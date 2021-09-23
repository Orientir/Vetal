import requests
from pprint import pprint as pp

# responce = requests.get('http://rzhunemogu.ru/RandJSON.aspx?1')
# if responce.status_code == 200:
#     text = responce.text.replace('{"content":"', '').replace('"}', '')
#     print(text)

# responce = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
# if responce.status_code == 200:
#     course_list = responce.json()
#     euro = course_list[1]
#     euro_buy = euro['buy']
#     euro_sale = euro['sale']
#     print(f'Buy - {euro_buy}, sale - {euro_sale}')
#     print(course_list)


# data = {'q':'Херсон', 'type': 'like', 'units': 'metric', 'APPID': '31b1cf0130115aa13950e5667d5ba0d4', 'lang': 'ru'}
# # responce =requests.get('http://api.openweathermap.org/data/2.5/weather', params=data)
# #
# # print(responce.json())

MOVIE_KEY = '149cc9ead676f0b1158bbb88868b8402'
url = 'https://api.themoviedb.org/3/trending/'
params = {'api_key': MOVIE_KEY, 'media_type': 'movie', 'time_window': 'week'}


responce = requests.get(url, params=params)
json = responce.json()
pp(json)