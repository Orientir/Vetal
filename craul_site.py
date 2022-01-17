from requests_html import HTMLSession

fail_domens = ['linkedin', 'pdf', 'adobe', 'google', 'yandex', 'youtube', 'facebook', 'instagram', 'twitter', 'apps', 'apple', 'tripadvisor', 'tiktok', 'itunes', 'music']
def craul(l):
    google_died_domen = 'google-died-domen.txt'
    domain = l.split('/')[2]

    session = HTMLSession()
    crawled_links = set()
    links_to_crawl = set()
    links_to_crawl.add(l)
    check_links = set()

    while True:
        try:
            if len(links_to_crawl) == 0:
                break
            url = links_to_crawl.pop()
            response = session.get(url)
            if len(check_links) > 0:
                try:
                    url_other = check_links.pop()
                    resp = session.get(url_other)
                except Exception as e:
                    print('***')
                    print('DIED ', url_other)
                    print('***')
                    with open(google_died_domen, 'a', encoding='utf-8') as f:
                        f.write(url_other + '\n')
                    break
            print(url)
            crawled_links.add(url)
            for link in response.html.absolute_links:
                if any(site for site in fail_domens if site in link):
                    continue
                if link in crawled_links:
                    continue
                if not domain in link and link.startswith('http'):
                    check_links.add(link)
                    continue
                links_to_crawl.add(link)

        except Exception as e:
            print("Oops, except")
            print(e)