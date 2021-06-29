# import random
#
# MAX_LIFE = 3
# life = 3
# def get_random(min=1, max=3):
#     return random.randint(min, max)
#
# def defeat_meteorit(life):
#     hit = get_random()
#     life -= hit
#     return life
#
#
# def defeat_bomb(life):
#     hit = 2
#     raund = 10
#     life -= hit
#     return (life, raund)

#
#
#
# life = defeat_meteorit(life)
# life = defeat_bomb(life)
#
#
# print(life)

from requests_html import HTMLSession

def check_result(word, meta, text, grade=20):
    if word in meta:
        # print("оценка за ключевое слово '\"' {0} '\"' {1} - {2}".format(word, text, grade))
        print(f"оценка за ключевое слово '\"' {word} '\"' {text} - {grade}")
        return grade
    else:
        print(f'Нет такого ключа в {text}')
        return 0


result_sym_title = 0
result_sym_description = 0
result_sym_h1 = 0
result_key_title = 0
result_key_description = 0
result_key_h1 = 0


while True:
    url = input('Enter URL or exit: ')

    if url.lower().startswith("exit"):
        print("Good Bye")
        exit()

    if ('http' in url) and ('//' in url):
        keyword = input('Enter Keyword: ')

    else:
        print('Not URL. Enter with http protocol!')
        break

    with HTMLSession() as session:
        resp = session.get(url)

    try:
        title = (str.lower(resp.html.xpath('//title')[0].text))
    except Exception as e:
        print('title not found on the page', e)
        title = ''

    try:
        description = resp.html.xpath('//meta[@name="description"]/@content')[0]
    except Exception as e:
        print('Description not found on the page', e)
        description = ''

    try:
        h1 = resp.html.xpath('//h1')[0].text
    except Exception as e:
        print('H1 not found on the page', e)
        h1 = ''

    print('*' * 50)
    print('TITLE:', title)
    print('*' * 50)
    print('DESCRIPTION:', description)
    print('*' * 50)
    print('H1:', h1)
    print('*' * 50)

    sym_title = len(title)
    sym_description = len(description)
    sym_h1 = len(h1)  # подсчет символов в h1
    sym_result = f'Букв в Title {sym_title}\n Букв в Description {sym_description}\n Букв в h1 {sym_h1}\n'

    print(sym_result)

    if sym_title <= 60:
        result_sym_title = 10
        print('оценка за к-во Title -', result_sym_title)
    elif 0 < sym_title < 30:
        print('Слишком короткий тайтл')

    if sym_description <= 170:
        result_sym_description = 10
        print('оценка за к-во description -', result_sym_description)
    elif 0 < sym_title < 160:
        print('Слишком короткий description')

    if sym_h1 <= 40:
        result_sym_h1 = 20
        print('оценка за к-во h1 -', result_sym_h1)
    elif 0 < sym_title < 20:
        print('Слишком короткий h1')

    # if keyword in title:
    #     result_key_title = 20
    #     print('оценка за ключевое слово', '\"' + keyword + '\"', 'в Title -', result_key_title)
    # else:
    #     print('Нет такого ключа в Title')

    result_key_title = check_result(keyword, title, 'в Title')

    # if keyword in description:
    #     result_key_description = 20
    #     print('оценка за ключевое слово', '\"' + keyword + '\"', 'в Description -', result_key_description)
    # else:
    #     print('Нет такого ключа в Description')

    result_key_description = check_result(keyword, description, 'в Description')

    # if keyword in h1:
    #     result_key_h1 = 20
    #     print('оценка за ключевое слово', '\"' + keyword + '\"', 'в H1 -', result_key_h1)
    # else:
    #     print('Нет такого ключа в h1')

    result_key_h1 = check_result(keyword, h1, 'в H1')

    print('*' * 50)

    sum_quality = result_sym_title + result_sym_description + result_sym_h1 + result_key_title + result_key_description + result_key_h1

    print('\nSEO Page Quality is:', sum_quality)


