# life = 3
#
# def check_life(life):
#     life -= 1
#     return life
#
#
# game = True
# while game:
#     print(life)
#
#     if True:
#         life = check_life(life)
#         if life > 0:
#             pass
#         else:
#             print("We loose")


# apples = 200
# bread = 100
# milk = 50
# vaucher = 50

# def actual_price(vaucher=0, **kwargs):
#     summa = 0
#     print(kwargs)
#     for i in kwargs.values():
#         summa += i
#     if summa - vaucher < 0:
#         return 0
#     return summa - vaucher
#
#
# check_price = actual_price(500, aplles=apples, bread=100, milk=50)
# print(check_price)

# 2x + 10 = 12 + (-10_

# def check_math(b, c, a=1):
#     return (c+b)/a
#
# print(check_math(2, 10, 12))
#
# error = {0: "spec.symbol"}
#
# city = input("Input city: ")
# age = int(input("Input age: "))
#
# about = {"name": name, "age": age, "city": city}
#
#
# def check_name(name):
#     if not name.istitle():
#         return False
#     for i in name:
#         if i.isdigit():
#             return False
#         elif i.isupper() and i.index(i) != 0:
#             return False
#         elif i in (".,:;!_*-+()/#¤%&)"):
#             return False
#         return True
#
# def about_human(kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} - {value}")
#
# while True:
#     name = input("Input name: ")
#     result = check_name(name)
#     if result:
#         break
#     else:
#         print("Try again, without *^@!")
#
# about_human(about)

from requests_html import HTMLSession
session = HTMLSession()

r = session.get('https://python.org/')
# all_links = [link for link in r.html.links if 'http' in link]
all_links = r.html.absolute_links
# a = r.html.xpath('//meta[@name="googlebot"]/@content')
# print(a)
# print(all_links)
# for i in all_links:
#     new = session.get(i)
#     links = new.html.absolute_links
#     print(links)

# while all_links:
#     new_links = []
#     for i in all_links:
#         new = session.get(i)
#         links = new.html.absolute_links
#         new_links = [*links]
#     print(new_links[0])
#     break
