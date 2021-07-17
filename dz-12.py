from time import time
from requests_html import HTMLSession
from reppy.robots import Robots
from pprint import pprint as pp

# from deco import time_decorator


session = HTMLSession()

crawled_links = set()

links_to_crawl = set()

to_continue = input('Продолжить сканировать старый сайт с прошлого места - <да>, или начать сканировать новый сайт - <нет>?')
if to_continue.lower() == 'нет':
    domain = input('Введите домен для краулинга: ')
    first_link = f'http://{domain}/'
    links_to_crawl.add(first_link)
    prepared_response = session.get(first_link, proxies={})
    first_link = prepared_response.url
else:
    read_to_crawl = open("links_to_crawl.txt", "r", encoding='utf-8').readlines()
    read_is_crawl = open("crawled_links.txt", "r", encoding='utf-8').readlines()

    links_to_crawl = set(x.strip() for x in read_to_crawl)
    crawled_links = set(x.strip() for x in read_is_crawl)

    first_link = links_to_crawl.pop()


domain = first_link.split('/')[2]

robots_link = f'https://{domain}/robots.txt'
robots = Robots.fetch(robots_link)

file_results = open('checking_results.txt', 'w', encoding='utf-8')


while True:
    try:

        if len(links_to_crawl) == 0:
            break
        url = links_to_crawl.pop()

        t1 = time()
        response = session.get(url)
        t2 = time()

        crawled_links.add(url+'\n')
        bad_parts = ['cdn-cgi', '.jpg', '.gif']

        for link in response.html.absolute_links:
            if domain not in link:
                continue
            if not robots.allowed(link, '*'):
                continue
            if any(x in link for x in bad_parts):
                continue
            if link in crawled_links:
                continue
            links_to_crawl.add(link+'\n')

        result = f'[{round(t2-t1, 2)} sec] [OK] {url}'
        print(result)

        file_results.write(result+'\n')
        file_results.flush()

    except KeyboardInterrupt:
        to_crawl = open("links_to_crawl.txt", "w", encoding='utf-8')
        is_crawl = open("crawled_links.txt", "w", encoding='utf-8')

        to_crawl.writelines(links_to_crawl)
        is_crawl.writelines(crawled_links)

        to_crawl.close()
        is_crawl.close()

        breakpoint()