import asyncio
import aiohttp
import random
from lxml import html
from requests_html import HTMLSession
from aiohttp_socks import ProxyType, ProxyConnector, ChainProxyConnector
from db import Page, objects


BAD_PARTS = {
    '.jpg', '.jpeg', '.png', '.gif', '/cdn-cgi', '.css',
    '.mp4', '.webm', '.ico', '/static/', '/media/', '/summernote/'
}


LINKS_QUEUE = set()
SCANNED_LINKS = set()


with open('../proxies.txt', 'r') as f:
    PROXIES = [line.strip() for line in f if line.strip()]

with open('../ua.txt', 'r') as f:
    USER_AGENTS = [line.strip() for line in f if line.strip()]

with open('keys.txt', 'r') as f:
    KEYS = ['+'.join(line.strip().split()) for line in f if line.strip()]


async def worker(domain):
    async with aiohttp.ClientSession() as session:
        while True:
            await asyncio.sleep(3)
            try:
                url = domain

                rand_headers = {'User-Agent': random.choice(USER_AGENTS)}

                resp = await session.get(url, headers=rand_headers)

                html_code = await resp.text()
                assert resp.status == 200

            except Exception as e:
                print(e, type(e))
                continue
            try:
                dom_tree = html.fromstring(html_code)
            except ValueError as e:
                print(e, type(e))
                continue

            try:
                content = dom_tree.xpath('//li[@class="b_algo"]')
            except Exception as e:
                print(e, type(e))

            for index, item in enumerate(content):
                link = item.xpath('//h2//a')[0].get("href")
                if any(part in link for part in BAD_PARTS):
                    break
                if not 'http' in link:
                    break

                try:
                    page_title = item.xpath('//h2//a')[0].text
                except:
                    page_title = ' '

                try:
                    session1 = HTMLSession()
                    response = session1.get(link)
                    page_h1 = response.html.xpath('//h1')[0].text
                except:
                    page_h1 = ' '


                page = {"url": link, "title": page_title.strip(), "h1": page_h1.strip()}
                print(page)
                try:
                    await objects.create(Page, **page)
                except Exception as e:
                    print(e)

            break


async def main():

    tasks = []
    for key in KEYS:
        new_domain = f'https://www.bing.com/search?q={key}&qs=n&form=QBRE&sp=-1&pq={key}&sc=8-6&sk=&cvid=F60291D325BA4D94BA4104B6116EF277'
        tasks.append(worker(new_domain))
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())