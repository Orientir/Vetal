'''Задача 4. Напишите программу с классом Car. Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
Напишите пять методов. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен». Второй — отключение автомобиля —
выводит сообщение «Автомобиль заглушен». Третий — присвоение автомобилю года выпуска. Четвертый метод — присвоение автомобилю типа. Пятый —
присвоение автомобилю цвета. Затем, добавьте еще один атрибут - "пробег" (по умолчанию == 0) и атрибут "бензин" (по умолчанию 30 - количество
литров в баке) и "объем бака" (по умолчанию 60).
Добавьте метод "ехать", аргументом которого будет расстояние в км, например go_car(self,
distance=15). Метод должен 1) определять, может ли машина ехать (есть ли бензин - читать дальше), если может - добавлять дистанцию к атрибуту
"пробег" и отнимать от атрибута "бензин" по формуле (литраж делим на километраж и умножаем на сто – л/км*100). Если машина ехать не может -
вывести текст "закончился бензин". Добавить методы для проверки бензина в баке, для проверки пробега автомобиля и для заправки автомобиля
(атрибуту "бензин" обновляем значение) '''

class Car():
    miles = 0
    gasoline = 0
    fuel_consumption = 0.9 # расход бензина на 1 километр
    on_engine = False

    def __init__(self, color, type, year, tank=60):
        self.color = color
        self.type = type
        self.year = year
        self.tank = tank

    def start(self):
        self.on_engine = True
        print('Автомобиль заведен')

    def stop(self):
        self.on_engine = False
        print("Автомобиль заглушен")
        self.show_parameters()

    def show_parameters(self):
        print(f"Miles - {self.miles}")
        print(f"Gasoline - {self.gasoline}")

    def go_car(self, distance=15):
        if not self.on_engine:
            self.start()
        need_gas = distance * self.fuel_consumption
        can_move = self.gasoline >= need_gas
        if can_move:
            self.gasoline -= need_gas
            self.miles += distance
            print("We go, we have gas: ", self.gasoline)
        else:
            could_charge = self.tank - self.gasoline
            print(f"the gasoline not enough, we have {self.gasoline} litres")
            litres = int(input(f"Input litres or 0 or 1. You can charge to {could_charge} litres "))

            while litres != 0 and litres > could_charge:
                litres = int(input(f"Input litres or 0. You can charge to {could_charge} litres "))

            if not litres:
                self.stop()
            elif litres == 1:
                self.gas_station()
            else:
                self.gas_station(litres)

    def gas_station(self, litres=None):
        self.gasoline += litres if litres else self.tank - self.gasoline
        print(f"We are charged, {self.gasoline} we have")

car = Car('черный', 'легковая', 2010)
# car1 = Car('red', 'легковая', 2000)

car.start()
car.go_car()
car.go_car(20)
car.go_car(40)
car.go_car(60)
car.go_car(80)
car.stop()



