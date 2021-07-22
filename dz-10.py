# task 1
# r = open("keywords.csv", "a", encoding='utf-8')
#
# with open("files/EnglishKeywords.txt", "r", encoding='utf-8') as f:
#     for line in f:
#         if 'sale' in line:
#             print(line)
#             r.write(line + '\n')
#             r.flush()
#
# f.close()

# task 2

from requests_html import HTMLSession
from reppy.robots import Robots



session = HTMLSession()
domain = input('Введите домен для краулинга: ')
main_link = f'http://{domain}/'

file = open("ready_links.txt", 'a', encoding="utf-8")

response = session.get(main_link)

robots_link = f'https://{domain}/robots.txt'

crawled_links = set()
links_to_crawl = set()
links_to_crawl.add(main_link)


robots = Robots.fetch(robots_link)

while True:
    try:
        if len(links_to_crawl) == 0:
            break
        url = links_to_crawl.pop()
        response = session.get(url)
        crawled_links.add(url)

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

    except:
        continue

print("file ready for using")