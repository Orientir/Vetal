url = 'https://www.bbc.com/news/science-environment-56799755'
title = 'nasa successfully flies small helicopter on Mars - BBC news'
description = 'The Ingenuity drone completes the first powered, controlled flight by an aircraft on another world.'
h1 = 'Nasa successfully flies small helicopter on Mars'
keyword = 'nasa news BBC Mars'

print ('URL -', url, '\n', 'TITLE -', title, '\n', 'DESCRIPTION -', description, '\n', 'H1 -', h1, '\n', 'KEYWORD -', keyword)

url_words = len(url.split())
url_letters = len(url)



title_words = len(title.split())
title_letters = len(title)



description_words = len(description.split())
description_letters = len(description)



h1_words = len(h1.split())
h1_letters = len(h1)





url_result = f'слов в url {url_words}, букв в url {url_letters}\n'
title_result = f'слов в title -  {title_words}, букв в title {title_letters}\n'
description_result = f'слов в description {description_words}, букв в description {description_letters}\n'
h1_result = f'слов в h1 {h1_words}, букв в h1 {h1_letters}\n'


print("----------------Подсчет: Вариант 1------------------")


print(url_result, title_result, description_result, h1_result)


print("----------------Подсчет: Вариант 2------------------")


result_count_words = 'слова в URL - {} слова в title - {}, слова в description - {}, слова в h1 - {}\n'.format(url_words, title_words, description_words, h1_words)

result_count_letter = 'Буквы в URL - {}, Буквы в title - {}, Буквы в description - {}, Буквы в h1 - {}'.format(url_letters, title_letters, description_letters, h1_letters)

print(result_count_words, result_count_letter)





print('----------------количество вхождений ключевых слов------------------')


count_title = title.lower().count('nasa')
count_description = description.lower().count('nasa')
count_h1 = h1.lower().count('nasa')


print('Ключевой запрос nasa в tittle - ', count_title,'|',
	'Ключевой запрос nasa в Description - ', count_description,'|',
	'Ключевой запрос nasa в H1 - ', count_h1)



print("----------------плотность ключевого слова в процентах------------------")

percent_title = 100 / title_words * count_title
percent_description = 100 / description_words * count_description
percent_h1 = 100 / h1_words * count_h1

print(f'плотность ключевого слова Nasa в Title - ',percent_title,'%\n',
	'плотность ключевого слова Nasa в Title - ', percent_description,'%\n',
  	'плотность ключевого слова Nasa в Title - ', percent_h1,'%')