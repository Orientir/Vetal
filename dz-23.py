import csv
import random
from peewee import *
from requests_html import HTMLSession
from slugify import slugify


class OlxParser:
   def __init__(self):
      self.start_url = 'https://www.olx.ua/'
      self.category_xpath = '//li/a[@data-id]/@href'
      self.proxies = []
      self.agents = []
      self.session = HTMLSession()
      self.result_file = 'olx_ads.csv'
      self.set_all_proxies()
      self.set_all_agents()

      self.fieldnames = ['ad_title', 'ad_date', 'ad_price',
                         'ad_photo', 'ad_link', 'ad_city']

   def set_all_proxies(self):
      with open('proxies.txt', 'r', encoding='utf-8') as f:
         self.proxies = [p.strip() for p in f if p.strip()]

   def set_all_agents(self):
      with open('ua.txt', 'r', encoding='utf-8') as f:
         self.agents = [x.strip() for x in f if x.strip()]

   def get_random_proxy(self):
      random_proxy = random.choice(self.proxies)
      return {'http': f'socks5://{random_proxy}',
              'https': f'socks5://{random_proxy}'}

   def get_random_headers(self):
      return {'User-Agent': random.choice(self.agents)}

   def get_category_links(self):
      headers = self.get_random_headers()
      response = self.session.get(self.start_url, headers=headers)
      links = response.html.xpath(self.category_xpath)
      return links

   def run(self):
      links = self.get_category_links()

      for link in links:
         headers = self.get_random_headers()
         resp = self.session.get(link, headers=headers)
         self.get_ads(resp)

   def get_ads(self, response):
      ad_blocks = response.html.xpath('//div[@class="offer-wrapper"]')
      with open(self.result_file, 'a', encoding="utf-8") as f:
         csv_writer = csv.DictWriter(f, self.fieldnames)
         for ad in ad_blocks:
            try:
               ad_title = ad.xpath('//h3')[0].text
               ad_date = ad.xpath('//p[@class="lheight16"]/small[2]')[0].text
               try:
                  ad_photo = ad.xpath('//img/@src')[0]
               except:
                  ad_photo = "no photo"
               ad_link = ad.xpath('//h3/a/@href')[0]
               ad_city = ad.xpath('//p[@class="lheight16"]/small[1]')[0].text
               try:
                  ad_price = ad.xpath('//p[@class="price"]')[0].text
                  price = float(ad_price.replace(' грн.', '').replace(' ', ''))
               except:
                  price = float(0)

               ad = {
                  'ad_title': ad_title,
                  'ad_date': ad_date,
                  'ad_price': price,
                  'ad_photo': ad_photo,
                  'ad_link': ad_link,
                  'ad_city': ad_city,
               }
               try:
                  csv_writer.writerow(ad)
               except Exception as e:
                  print("EXCEPT CSV ", e)
               Olx.create(**ad)
            except Exception as e:
               print(e)
            finally:
               print(ad_link)


db = PostgresqlDatabase('library', host='88.198.172.182', port=5432, user='py4seo', password='PY1111forSEO')
db_table_olx = slugify("Виталий Козаченко")
db_table_category = "Category"


class Category(Model):
   name = CharField(max_length=55)
   description = CharField(max_length=255)

   class Meta:
      database = db


class Olx(Model):
   ad_title = CharField()
   ad_date = CharField()
   ad_price = FloatField()
   ad_photo = CharField()
   ad_link = CharField()
   ad_city = CharField()

   category = ForeignKeyField(Category, related_name='articles')

   class Meta:
      database=db
      db_table=db_table_olx

db.connect()

#db.create_tables([Olx])
# parser = OlxParser()
# parser.run()
