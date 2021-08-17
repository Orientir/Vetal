from requests_html import HTMLSession
from reppy.robots import Robots
import time

class SiteCrawler:
    session = HTMLSession()
    crawled_links = set()
    links_to_crawl = set()

    ready_links = 'ready_links.txt'
    file_crawled_links = "file_crawled_links.txt"
    file_to_crawl_links = "file_to_crawl_links.txt"

    def __init__(self, domain, is_new):
        self.domain = domain
        self.main_link = f'http://{domain}/'
        self.links_to_crawl.add(self.main_link)
        self.robots = self.get_robots()
        self.is_new = is_new

        print("It was init")
        time.sleep(1)

    def get_robots(self):
        robots_link = f'https://{self.domain}/robots.txt'

        print("get_robots")
        time.sleep(1)
        return Robots.fetch(robots_link)

    def read_file_crawled_links(self):
        with open(self.file_crawled_links, 'r', encoding='utf-8') as f:
            f_cr = f.readlines()
            self.crawled_links = set(x.strip() for x in f_cr)
        print("read_file_crawled_links")
        time.sleep(1)

    def read_links_to_crawl(self):
        with open(self.file_to_crawl_links, 'r', encoding='utf-8') as f:
            f_cr = f.readlines()
            self.links_to_crawl = set(x.strip() for x in f_cr)
        print("read_links_to_crawl")
        time.sleep(1)

    def save_file_crawled_links(self):
        with open(self.file_crawled_links, 'w', encoding='utf-8') as f:
            for link in self.crawled_links:
                f.write(link+'\n')
                f.flush()
        print("save_file_crawled_links")
        time.sleep(1)

    def save_links_to_crawl(self):
        with open(self.file_to_crawl_links, 'w', encoding='utf-8') as f:
            for link in self.links_to_crawl:
                f.write(link+'\n')
                f.flush()
        print("save_links_to_crawl")
        time.sleep(1)

    def parse(self):
        print("parse")
        time.sleep(1)
        try:
            if len(self.links_to_crawl) == 0:
                pass
            else:
                url = self.links_to_crawl.pop()
                response = self.session.get(url)
                self.crawled_links.add(url)
                print(url)
                for link in response.html.absolute_links:

                    if self.domain not in link:
                        continue
                    if not self.robots.allowed(link, '*'):
                        continue
                    if link in self.crawled_links:
                        continue
                    self.links_to_crawl.add(link)
                if self.is_new:
                    file = open(self.ready_links, 'w', encoding="utf-8")
                else:
                    file = open(self.ready_links, 'a', encoding="utf-8")
                file.write(url + '\n')
                file.flush()

        except:
            print("parse except")
            time.sleep(1)
            self.save_file_crawled_links()
            self.save_links_to_crawl()


site = SiteCrawler('b-options.com', True)
site.parse()