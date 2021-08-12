"""
1. Вводим ключевую фразу из консоли.
2. Получаем ТОП-10 Google по запросу.
3. Заходим на страницы всех сайтов из ТОП-10 и скачиваем текст.
4. Анализируем текст и генерируем задание для копирайтера.
5. Отправляем задание на email адрес.
"""

from core import (
    google_scraper, get_text,
    texts_analyzer, COPYWRITER_TASK,
    send_email,
    text_with_count_income,
    delete_numbers
)


def tz_on_mail(keyword=None):
    while not keyword:
        keyword = input('Enter key phrase: ')

    links = google_scraper(keyword)
    texts = dict()

    for link in links:
        texts[link] = get_text(link)

    top3 = list(texts.values())[:3]
    reference = links[:3]

    keywords_main, count_income_main = texts_analyzer(texts.values())
    keywords_secondary, count_income_secondary = texts_analyzer(top3)

    keywords_secondary.difference_update(keywords_main)

    ready_keyword_main = text_with_count_income(keywords_main, count_income_main)
    ready_keyword_secondary = text_with_count_income(keywords_secondary, count_income_secondary)

    keywords_main_no_numbers = delete_numbers(keywords_main)

    task_text = COPYWRITER_TASK.format(
        keywords_main='\n'.join(ready_keyword_main),
        keywords_secondary='\n'.join(ready_keyword_secondary),
        title=keyword.upper(),
        keywords_title='\n'.join(keywords_main_no_numbers),
        reference='\n'.join(reference)
    )

    print(task_text)

    send_email(task_text, "ya.orient@gmail.com")


if __name__ == '__main__':
    tz_on_mail()