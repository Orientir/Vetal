from requests_html import HTMLSession


file = 'photo.txt'
session = HTMLSession()
url = 'https://jsonplaceholder.typicode.com/photos'

r = session.get(url)
if r.status_code == 200:
    data = r.json()
    with open(file, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(item['url']+'\t')
            f.write(item['thumbnailUrl']+'\n')
            f.flush()
else:
    print('Some went wrong')
