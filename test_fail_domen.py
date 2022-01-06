from requests_html import HTMLSession
from requests.exceptions import ConnectionError
from time import sleep
from random import randint
from pprint import pprint as pp
from craul_site import craul

google_top = 'google-top-100.txt'
google_died_domen = 'google-died-domen.txt'
google_keys = 'google-keys.txt'

fail_domen = ['google', 'yandex', 'youtube', 'facebook', 'instagram', 'twitter']

with open(google_keys, 'r', encoding='utf-8') as f:
    keys = f.readlines()
if keys:
    key, index = tuple(keys[-1].split(';'))

if keys:
    question = (input(f'Continue {key} parse or start new? Y - Continue, N - start new : ')).lower()

    if question == 'n':
        key = input('Input key: ')
        with open(google_keys, 'a', encoding='utf-8') as f:
            f.write(key+'\n')
else:
    key = input('Input key: ')
    with open(google_keys, 'a', encoding='utf-8') as f:
        f.write(key + '\n')

google = f'https://www.google.com/search?q={key}&num=100&hl=en'

session = HTMLSession()
resp = session.get(google)
html_snipets = resp.html.xpath('//div[@class="g"]')

for link in html_snipets:
    url = link.xpath('//div[@class="yuRUbf"]/a[1]/@href')[0]
    try:
        response = session.get(url)
        all_links = response.html.absolute_links
        for l in all_links:
            craul(l)
            # try:
            #     respons = session.get(l)
            # except ConnectionError as e:
            #     print('Inside link ', l)
            #     with open(google_died_domen, 'a', encoding='utf-8') as f:
            #         f.write(l + '\n')
            # except Exception as e:
            #     print(e)
            # second = randint(1, 5)
            # sleep(second)
    except ConnectionError as e:
        print('ConnectionError', url)
        with open(google_top, 'a', encoding='utf-8') as f:
            f.write(url+'\n')
    except Exception as e:
        print('MAIN ', e)
    second = randint(1, 5)
    sleep(second)

print('**********************')
print('TASK DONE')
print('**********************')

