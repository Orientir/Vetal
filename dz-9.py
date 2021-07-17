from requests_html import HTMLSession
from reppy.robots import Robots

from pprint import pprint
from usp.tree import sitemap_tree_for_homepage

import requests
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

# urls = [
#     'https://habr.com/search/',
#     'https://habr.com/ru/company/southbridge/blog/489628/',
#     'https://habr.com/ru/company/skyeng/blog/487764/',
#     'https://habr.com/register/',
#     'https://habr.com/ru/users/gbougakov/',
#     'https://habr.com/ru/search/?q=django',
#     'https://habr.com/ru/post/486998/',
# ]
#
# robots = Robots.fetch('https://habr.com/robots.txt')
# sitemap = robots.sitemaps

# open_urls = []
#
# for url in urls:
#     is_open = robots.allowed(url, 'my-user-agent')
#     print(is_open)
#     if is_open:
#         open_urls.append(url)
#
# print(open_urls)

# session = HTMLSession()

# open_bot = [] # ссылки открыты для индексации гугла
# r = session.get('https://b-options.com/')
# all_links = set(r.html.absolute_links)
# length = len(all_links)
# print(length)
#
# for link in all_links:
#     googlebot = r.html.xpath('//meta[@name="googlebot"]/@content')
#     if not googlebot:
#         open_bot.append(link)
#     new_r = session.get(link)
#     new_links = set(new_r.html.absolute_links)
#     print(len(new_links))

# def rec_func(number):
#     if number>0:
#         print(number)
#     else:
#         return 1
#     rec_func(number-1)
#
# rec_func(5)

# robots = Robots.fetch('https://b-options.com/robots.txt')
# tree = sitemap_tree_for_homepage('https://b-options.com/')
# pages = [page.url for page in tree.all_pages()]

# for page in tree.all_pages():
#     pages.append(page.url)
#
# pages = set(pages)
#
# pp(pages)

# print(len(pages))



# def get_source(url):
#     try:
#         session = HTMLSession()
#         response = session.get(url)
#         return response
#
#     except Exception as e:
#         print(e)
#
# def get_url_sitemap(url):
#     try:
#         robots = Robots.fetch(f'{url}robots.txt')
#         sitemap = robots.sitemaps
#         return sitemap[0] if sitemap else f"{url}sitemap.xml"
#
#     except Exception as e:
#         print(e)
#         return f"{url}sitemap.xml"
#
# def scrape_sitemap(url):
#     df = pd.DataFrame(columns=['url'])
#
#     sitemap = get_url_sitemap(url)
#     print(sitemap)
#     if sitemap:
#         response = get_source('https://www.deezer.com/sitemap.xml')
#
#         with response as r:
#             urls = r.html.find("loc", first=False)
#
#             for url in urls:
#                 row = {'url': url.text}
#
#                 df = df.append(row, ignore_index=True)
#
#     return df

# http://flyandlure.org/sitemap.xml


# url = "https://b-options.com/"

# df = scrape_sitemap(url)
# df.to_csv("sitemap.csv", index=False)
# df.tail(10)

session = HTMLSession()
domen = input("Input domen: ") # binaryoptionsdailyreview.com
response = session.get(f'http://{domen}/sitemap.xml')
print(response)

links = []

with response as r:
    urls = r.html.find("loc", first=False)
    print(len(urls), " --- sitemap")

    for url in urls:
        link = url.text
        resp = session.get(link)
        googlebot = resp.html.xpath('//meta[@name="googlebot"]/@content')
        if not googlebot:
            links.append(url.text)

pprint(links)
print(len(links), " --- googlebot")