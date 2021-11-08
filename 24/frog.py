from time import sleep
from queue import Queue
from threading import Lock, Thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from db import db_saver

import time


BAD_PARTS = {'.jpg', '.jpeg', '.png', '.gif', '/cdn-cgi'}

locker = Lock()

LINKS_QUEUE = Queue()
SCANNED_LINKS = set()


saver = db_saver()
saver.__next__()


def worker(domain):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(options=option)
    while True:
        if LINKS_QUEUE.qsize() == 0:
            sleep(10)
            if LINKS_QUEUE.qsize() == 0:
                with locker:
                    saver.send('save')
                break
            continue

        url = LINKS_QUEUE.get()
        SCANNED_LINKS.add(url)

        try:
            resp = driver.get(url)

        except Exception as e:
            print(e, type(e))
            continue

        try:
            # page_title = resp.html.xpath('//title')[0].text
            page_title = driver.title
        except IndexError:
            page_title = 'Not Found'

        try:
            # page_h1 = resp.html.xpath('//h1')[0].text
            page_h1 = driver.find_elements_by_xpath('//h1')[0].text
        except IndexError:
            page_h1 = 'Not Found'

        page = {"url": url, "title": page_title, "h1": page_h1}

        with locker:
            try:
                saver.send(page)
            except:
                print('EXCEPT: ', page)

        print('OK', url)

        with locker:
            with open('results.csv', 'a') as f:
                try:
                    f.write(f'{url}\t{page_title}\t{page_h1}\n')
                except:
                    f.write(f'EXCEPT: {url}\n')

        all_links = driver.find_elements_by_xpath("//a[@href]")
        for link in all_links:
            # link = link.split('#')[0]
            link = link.get_attribute("href")
            if domain not in link:
                continue
            if link in SCANNED_LINKS:
                continue
            if any(part in link for part in BAD_PARTS):
                continue

            LINKS_QUEUE.put(link)


def main():
    domain = input('Enter domain: ')
    home_page = f'https://{domain}/'
    LINKS_QUEUE.put(home_page)

    thread = 100
    # with ThreadPoolExecutor(max_workers=thread) as executor:
    #     for _ in range(thread):
    #         executor.submit(worker, domain)

    for _ in range(thread):
        Thread(target=worker, args=(domain, )).start()


if __name__ == '__main__':
    main()