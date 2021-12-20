import random
import datetime
from time import sleep
from time import time
from requests_html import HTMLSession

from peewee import *
db = PostgresqlDatabase('mydatabase', host='localhost',  port=5432, user='postgres', password='postgres')

class Page(Model):
    title = CharField(max_length=1024)
    title_len = IntegerField()
    response_time = FloatField()
    domain = CharField(max_length=1024, index=True)
    description = CharField(max_length=1024)
    description_len = IntegerField()
    h1 = CharField(max_length=1024)
    url = CharField(max_length=1024)
    scanned = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        table_name = 'less_27'

session = HTMLSession()
key = 'online cashback service'
engine_link = f'https://www.google.com/search?q={key}&num=100&hl=en'

resp = session.get(engine_link)

html_snipets = resp.html.xpath('//div[@class="g"]')

title = title_len = response_time = domain = description = description_len = h1 = url = 'Not  found'

for n, html_item in enumerate(html_snipets, start=1):
    try:
        url = html_item.xpath('//div[@class="yuRUbf"]/a[1]/@href')[0]
        try:
            domain = url.split('/')[2]
        except Exception as e:
            print(f"EXCEPTION domain: {e}")
        t1 = time()
        link_resp = session.get(url)
        t2 = time()
        try:
            title = link_resp.html.xpath('//title')[0].text
        except Exception as e:
            print(f"EXCEPTION title: {e}")
        title_len = len(title)
        try:
            description = link_resp.html.xpath('//meta[@name="description"]/@content')[0]
        except Exception as e:
            print(f"EXCEPTION description: {e}")
        description_len = len(description)
        try:
            h1 = link_resp.html.xpath('//h1')[0].text
        except Exception as e:
            print(f"EXCEPTION h1: {e}")
        response_time = round(t2 - t1, 2)
        print('response_time ', response_time, type(response_time))
        page = Page.create(title=title, title_len=title_len, response_time=response_time,
                           domain=domain, description=description, description_len=description_len, h1=h1, url=url)
        print(f"SUCCESS: {domain}")
    except Exception as e:
        print(f"EXCEPTION: {e}")



request_random_timeout = random.randint(5, 15)

print(f'[OK] {key} | sleep: {request_random_timeout} sec')

sleep(request_random_timeout)