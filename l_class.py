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
from reppy.robots import Robots

len_title = [60, 30]
len_description = [170, 160]
len_h1 = [40, 20]
grade_title = grade_description = 10
grade_h1 = 20

class Seo():
    meta = {'title': [len_title, grade_title],
            'description': [len_description, grade_description],
            'h1': [len_h1, grade_h1]}

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
        self.meta['title'].append(str.lower(self.response.html.xpath('//title')[0].text))
        self.meta['description'].append(self.response.html.xpath('//meta[@name="description"]/@content')[0])
        self.meta['h1'].append(self.response.html.xpath('//h1')[0].text)

    def check_sym(self, meta_name):
        meta_object = self.meta[meta_name]
        length = len(meta_object[2])
        if 0 < length < meta_object[0][1]:
            print(f'Слишком короткий {meta_name}')
            self.sym_title = 0
        elif length <= meta_object[0][0]:
            print(f'оценка за к-во {meta_name} - {meta_object[1]}')
            self.sym_title = meta_object[1]

    def get_all_information(self):
        pass



object = Seo('https://www.deezer.com/', 'python')
is_valid = object.check_url()
if is_valid:
    object.set_meta()
    object.check_sym('title')
    object.check_sym('description')
    object.check_sym('h1')
    print("*************")



