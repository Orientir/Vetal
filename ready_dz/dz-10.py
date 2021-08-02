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

#response = session.get(main_link)


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