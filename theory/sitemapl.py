from requests_html import HTMLSession
from reppy.robots import Robots

from pprint import pprint

# session = HTMLSession()
#
# r = session.get('https://habr.com/')
# all_links = set(r.html.absolute_links)
# without_links = [link for link in all_links if (not '#' in link) and ('https://habr.com/' in link)]
# with_links = [link for link in all_links if '#' in link]
#
# pprint(without_links)

session = HTMLSession()

# robots = Robots.fetch('http://flyandlure.org/robots.txt')
# sitemap = robots.sitemaps
# print(sitemap)

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