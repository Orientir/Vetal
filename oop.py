from dateutil.relativedelta import relativedelta
import datetime

class Family:
    def __init__(self, surname, address):
        self.surname = surname
        self.address = address

    def get_surname(self):
        return self.surname


class Person(Family):
    def __init__(self, birth, name, surname, weight=30, address='Kiev'):
        Family.__init__(self, surname, address)
        self.birth = birth
        self.name = name
        self.weight = weight

    def __str__(self):
        return self.get_surname()

    def get_surname(self):
        return self.name + ' ' + self.surname

    def get_age(self):
        age = datetime.datetime.now() - relativedelta(years=self.birth)
        return age.year

    def set_weight(self, weight):
        self.weight = weight

    def __del__(self):
        print("Object delete", self.name)

object = Person(birth=1900, name='Max', surname="Ivanov")
# del object

object2 = Person(birth=1990, name='Vasya', surname="Petrov", weight=60, address='Odessa')
print(object2)
name2 = object2.get_surname()
age = object2.get_age()
weight = object2.weight
print(name2, age, object2.weight)
object2.set_weight(80)
print(name2, age, object2.weight)
