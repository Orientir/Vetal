from time import time
from requests_html import HTMLSession
from pprint import pprint as pp

def craul(l):
    google_died_domen = 'google-died-domen.txt'
    domain = l.split('/')[2]

    session = HTMLSession()
    crawled_links = set()
    links_to_crawl = set()
    links_to_crawl.add(l)

    # if question.lower() == 'n':
    #     domain = input('Введите домен для краулинга: ')
    #     main_link = f'http://{domain}/'
    #     links_to_crawl.add(main_link)
    #     file = open("ready_links.txt", 'w', encoding="utf-8")
    # elif question.lower() == 'y':
    #     file = open("ready_links.txt", 'a', encoding="utf-8")
    #     with open("file_crawled_links.txt", 'r', encoding='utf-8') as f:
    #         f_cr = f.readlines()
    #         crawled_links = set(x.strip() for x in f_cr)
    #     with open("file_to_crawl_links.txt", 'r', encoding='utf-8') as f:
    #         f_cr = f.readlines()
    #         links_to_crawl = set(x.strip() for x in f_cr)
    #
    #     domain = links_to_crawl.pop().split('/')[2]
    #     links_to_crawl.add(domain)

    while True:
        try:
            if len(links_to_crawl) == 0:
                break
            url = links_to_crawl.pop()
            try:
                response = session.get(url)
            except ConnectionError as e:
                print('***')
                print('DIED ', url)
                print('***')
                with open(google_died_domen, 'a', encoding='utf-8') as f:
                    f.write(url + '\n')
            print(url)
            crawled_links.add(url)
            for link in response.html.absolute_links:
                if domain in link:
                    continue
                if link in crawled_links:
                    continue
                links_to_crawl.add(link)
            # file.write(url + '\n')
            # file.flush()

        except Exception as e:
            print("Oops, except")
            print(e)
            # with open("file_crawled_links.txt", 'w', encoding='utf-8') as f:
            #     for link in crawled_links:
            #         f.write(link + '\n')
            #         f.flush()
            #
            # with open("file_to_crawl_links.txt", 'w', encoding='utf-8') as f:
            #     for link in links_to_crawl:
            #         f.write(link + '\n')
            #         f.flush()
            break