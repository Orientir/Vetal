from time import time
from requests_html import HTMLSession
from reppy.robots import Robots
from pprint import pprint as pp

question = input("input Y - continue, N - new site")

session = HTMLSession()
crawled_links = set()
links_to_crawl = set()

if question.lower() == 'n':
    domain = input('Введите домен для краулинга: ')
    main_link = f'http://{domain}/'
    links_to_crawl.add(main_link)
    file = open("ready_links.txt", 'w', encoding="utf-8")
elif question.lower() == 'y':
    file = open("ready_links.txt", 'a', encoding="utf-8")
    with open("file_crawled_links.txt", 'r', encoding='utf-8') as f:
        f_cr = f.readlines()
        crawled_links = set(x.strip() for x in f_cr)
    with open("file_to_crawl_links.txt", 'r', encoding='utf-8') as f:
        f_cr = f.readlines()
        links_to_crawl = set(x.strip() for x in f_cr)

    domain = links_to_crawl.pop().split('/')[2]
    links_to_crawl.add(domain)
else:
    print("ERROR, try again")

robots_link = f'https://{domain}/robots.txt'
robots = Robots.fetch(robots_link)

print("Start work")
while True:
    try:
        if len(links_to_crawl) == 0:
            break
        url = links_to_crawl.pop()
        response = session.get(url)
        crawled_links.add(url)
        print(url)
        for link in response.html.absolute_links:

            if domain not in link:
                continue
            if not robots.allowed(link, '*'):
                continue
            if link in crawled_links:
                continue
            links_to_crawl.add(link)
        file.write(url + '\n')
        file.flush()

    except Exception as e:
        print("Oops, except")
        print(e)
        with open("file_crawled_links.txt", 'w', encoding='utf-8') as f:
            for link in crawled_links:
                f.write(link+'\n')
                f.flush()

        with open("file_to_crawl_links.txt", 'w', encoding='utf-8') as f:
            for link in links_to_crawl:
                f.write(link+'\n')
                f.flush()
        break

print("file ready for using")



#task 2

import random
from time import sleep
from requests_html import HTMLSession
from site_score import find_score


website = 'https://py4you.com/'

domain = website.split('/')[2]

results_format = 'Keyword\tUrl\tPosition\tTitle\tDescription\tSeo Score\tSeo Score Top 3\n'


with open('keywords.txt', 'r', encoding='utf-8') as f:
    keys_to_scan = [line.strip() for line in f]


with open('positions.csv', 'r', encoding='utf-8') as f:
    keys_scanned = set([line.split('\t')[0] for line in f])


r_file = open('positions.csv', 'a', encoding='utf-8')

r_file.write(results_format)

session = HTMLSession()

for key in keys_to_scan:
    score_top = 0

    if key in keys_scanned:
        continue

    engine_link = f'https://www.google.com/search?q={key}&num=100&hl=en'
    #engine_link = f'https://www.bing.com/search?q={key}&count=50'

    resp = session.get(engine_link)

    html_snipets = resp.html.xpath('//div[@class="g"]')
    #html_snipets = resp.html.xpath('//li[@class="b_algo"]')

    position = link = title = description = score = 'not-found'

    for n, html_item in enumerate(html_snipets, start=1):
        href = html_item.xpath('//div[@class="yuRUbf"]/a[1]/@href')[0]
        #href = html_item.xpath('//h2/a/@href')[0]
        # print(n, html_item, href)
        if domain in href:
            link = href
            title = html_item.xpath('//h3/text()')[0]
            #title = html_item.xpath('//h2')[0].text
            description = html_item.xpath('//div[@class="IsZvec"]')[0].text
            #description = html_item.xpath('//div[@class="b_caption"]/p')[0].text
            position = n
            score = find_score(href, key)
        index = n
        if index <= 3:
            score_top += find_score(href, key)
            # print(position, title, description)

    # print(position, title, description)
    average_score_top = score_top/3
    key_result = f'{key}\t{link}\t{position}\t{title}\t{description}\t{score}\t{average_score_top}\n'

    r_file.write(key_result)

    request_random_timeout = random.randint(5, 15)

    print(f'[OK] {key} | sleep: {request_random_timeout} sec')

    sleep(request_random_timeout)