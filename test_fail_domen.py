from requests_html import HTMLSession
from time import sleep
from random import randint
from craul_site import craul

google_top = 'google-top-100.txt'
google_died_domen = 'google-died-domen.txt'
google_keys = 'google-keys.txt'

fail_domens = ['linkedin', 'pdf', 'adobe', 'google', 'yandex', 'youtube', 'facebook', 'instagram', 'twitter', 'apps', 'apple', 'tripadvisor', 'tiktok', 'itunes', 'music']

with open(google_keys, 'r', encoding='utf-8') as f:
    keys = f.readlines()
if keys:
    last_element = keys[-1] if keys[-1] != "" else keys[-2]
    key, index = tuple(last_element.split(';'))
    index = int(index)

if keys:
    question = (input(f'Continue {key} parse or start new? Y - Continue, N - start new : ')).lower()

    if question == 'n':
        key = input('Input key: ')
else:
    key = input('Input key: ')
    question = 'no question'

google = f'https://www.google.com/search?q={key}&num=100&hl=en'

session = HTMLSession()
resp = session.get(google)
html_snipets = resp.html.xpath('//div[@class="g"]')

if question == 'y':
    html_snipets = html_snipets[index:]

for index, link in enumerate(html_snipets):
    try:
        url = link.xpath('//div[@class="yuRUbf"]/a[1]/@href')[0]
        with open(google_top, 'a', encoding='utf-8') as f:
            f.write(url + '\n')
        if any(site for site in fail_domens if site in url):
            continue
        try:
            response = session.get(url)
            all_links = response.html.absolute_links
            for l in all_links:
                craul(l)
        except Exception as e:
            with open(google_died_domen, 'a', encoding='utf-8') as f:
                f.write(url + '\n')
        second = randint(1, 5)
        sleep(second)
    except KeyboardInterrupt as e:
        with open(google_keys, 'a', encoding='utf-8') as f:
            f.write(key + ";" + str(index) + '\n')
        break
    except Exception as e:
        print(e)
        with open(google_keys, 'a', encoding='utf-8') as f:
            f.write(key + ";" + str(index) + '\n')
else:
    with open(google_keys, 'a', encoding='utf-8') as f:
        f.write(key + ";" + "100" + '\n')
print('**********************')
print('TASK DONE')
print('**********************')

