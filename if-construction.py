# if-elif-else, if if if if

# age = 50
#
# if age <=3:
#     print("you are child")
# elif age <=6:
#     print("childgarden")
# elif age <=17:
#     print("school")
# elif age <=23:
#     print("univer")
# elif age <=60:
#     print("work")
# elif age <=100:
#     print("pencia")
# else:
#     print("cool")

# key_user = input("input season ")

# month = {1: ["january", "Winter"], 2: ["february", "winter"]} #

month = {"Winter": [{1: "january"}, {2: "february"}, {3: "march"}], "Summer": ["february", "winter"]} #

# print(f"Month: {month[number][0]}, season: {month[number][1]}")


# for key, value in month.items():  # "string", range, [], (), {}
#     if key == key_user:
#         print(value[0])

# life = 3
# game_loop = True # пока мы играем
#
# while game_loop:
#     if life == 0:
#         game_loop = False

# salary = 1500
#
# shop = True
#
# while salary > 0:
#     money = int(input("Input money"))
#     if salary - money < 0: #  300    500
#         print("Денег не хватило")
#     else:
#         salary -= money
#         print(f"Мы купили что-то, у нас осталось {salary}")

salary = 1000
cash = 500

# result = 2
# i = 0  # counter

while salary > 0 and cash > 0:  #  True or False = True, True or True = True, False or False = False
    money = 500                 #  True and True = True,       False
    if salary == 0:
        cash -= money
        print("cash - money")
    else:
        salary -= money
        print("salary - money")


for i in range(1, 10):
    if i == 5:
        continue
    print(i)
