# class People:
#     def __init__(self, birth, name, surname):
#         self.birth = birth
#         self.name = name
#         self.surname = surname
#
#     def about_myself(self, string="About me "):
#         print(f'{string} - {self.name} {self.surname} - {self.birth}')
#
# p1 = People(1995, "Max", "Ivanov")
# p1.set_keywora("key")
# p1.get_sym_ttitle()
#
# print("---------------")
#
# p2 = People(2000, "Denis", "Petrov")
# p2.about_myself()
from requests_html import HTMLSession

class Seo():
    len_title = [60, 30]
    len_description = [170, 160]
    len_h1 = [40, 20]
    grade_title = grade_description = 10
    grade_h1 = 20

    result_grade_title = 0
    result_grade_description = 0
    result_grade_h1 = 0

    def __init__(self, url, keyword):
        self.url = url
        self.keyword = keyword

    def check_url(self):
        try:
            with HTMLSession() as session:
                resp = session.get(self.url)
                self.response = resp
            return True
        except:
            return False

    def set_meta(self):
        self.title = str.lower(self.response.html.xpath('//title')[0].text)
        self.description = self.response.html.xpath('//meta[@name="description"]/@content')[0]
        self.h1 = self.response.html.xpath('//h1')[0].text

    def check_sym(self, sym, list_count, grade, result, text):
        if 0 < sym < list_count[1]:
            print(f'Слишком короткий {text}')
        elif sym <= list_count[0]:
            print(f'оценка за к-во {text} - {grade}')
            result = grade

    def get_all_information(self):
        pass



object = Seo('https://python.org/', 'python')
is_valid = object.check_url()
if is_valid:
    object.set_meta()
    object.check_sym(len(object.title), object.len_title, object.grade_title, object.result_grade_title, 'title')
    object.check_sym(len(object.description), object.len_description, object.grade_description, object.result_grade_description, 'description')
    object.check_sym(len(object.h1), object.len_h1, object.grade_h1, object.result_grade_h1, 'h1')


