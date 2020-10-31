'''
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
'''
from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self, __color):
        self.__color = __color

    def running(self):
        colors = ['красный', 'желтый', 'зеленый']
        for i in cycle(colors):
            if i == self.__color and i == 'красный':
                print(f'\033[31m{i}')
                sleep(7)
                self.__color = 'желтый'
            if i == self.__color and i == 'желтый':
                print(f'\033[33m{i}')
                sleep(2)
                self.__color = 'зеленый'
            if i == self.__color and i == 'зеленый':
                print(f'\033[36m{i}')
                sleep(1)
                self.__color = 'красный'

red = TrafficLight('желтый')
red.running()
'''
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
'''
class Road:
    __massa = 20
    __thickness = 3
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def road_massa(self):
        print(f'Масса Крымского моста: {int((self.__length * self.__width * Road.__massa * Road.__thickness)/1000)}т.')

krym_road = Road(19000, 100)
krym_road.road_massa()

'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:
    def __init__(self, name, surname, position, income: dict):
        self.name= name
        self.surname = surname
        self.position = position
        self.__income = income

    def get_total_income(self):
        print(f'Совокупный доход сотрудника: {sum(self.__income.values())}')


class Position(Worker):
    def __init__(self, name, surname, position, income: {"wage": int, "bonus": int}):
        super().__init__(name=name, surname=surname, position=position, income=income)

    def get_full_name(self):
        print(f'Имя сотрудника: {self.name} {self.surname}. Должность {self.position}')


kirill = Position('Kirill', 'Smirnov', 'intern', {"wage": 50000, "bonus": 20000})
kirill.get_full_name()
kirill.get_total_income()
Maxim = Position('Maxim', 'Valov', 'military',{'wage': 60000, 'bonue':30000})
Maxim.get_full_name()
Maxim.get_total_income()

'''
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''


class Car:
    def __init__(self, speed, color, name, is_police:bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn_direction(self, direction:str):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'{self.name} едет со скоростью  {self.speed} км/ч')

    def police_or_not(self):
        if self.is_police:
            print(f'{self.name} полицейская машина')
        else:
            print(f'{self.name} не полицейская машина')


class TownCar(Car):
    def __init__(self,  speed, color, name, is_police=False):
        super().__init__(speed=speed, color=color, name=name, is_police=is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} едет со скоростью {self.speed} км/ч - привышение скорости!\n\tЛимит 60 км/ч')
        else:
            print(f'{self.name} едет с допустимой скоростью до 60 км/ч')


class SportCar(Car):
    def __init__(self,  speed, color, name, is_police=False):
        super().__init__(speed=speed, color=color, name=name, is_police=is_police)

class WorkCar(Car):
    def __init__(self,  speed, color, name, is_police=False):
        super().__init__(speed=speed, color=color, name=name, is_police=is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} едет со скоростью {self.speed} км/ч - привышение скорости!\n\tЛимит 40 км/ч')
        else:
            print(f'{self.name} едет с допустимой скоростью до 40 км/ч')

class PoliceCar(Car):
    def __init__(self,  speed, color, name, is_police=True):
        super().__init__(speed=speed, color=color, name=name, is_police=is_police)


Dodge = SportCar(250, 'green', 'Dodge')
Dodge.police_or_not()
ferrari = WorkCar(200, 'red', 'Ferrari')
ferrari.go()
ferrari.show_speed()
ferrari.police_or_not()
ferrari.turn_direction('направо')
ferrari.stop()
lada = PoliceCar(50, 'white', 'Vesta')
lada.police_or_not()
tiguan = TownCar(130, 'black', 'Tiguan')
tiguan.police_or_not()
tiguan.show_speed()
tiguan.speed = 35
bmw = TownCar(35, 'gray', 'BMW')
bmw.show_speed()

'''
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисокви {self.title}')

class Pen(Stationery):
    def draw(self):
        print(f'Рисуем ручкой {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем карандашом {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Рисуем маркером {self.title}')

sample = Stationery('дерево')
sample.draw()
pen = Pen('лошадь')
pen.draw()
pencil = Pencil('собака')
pencil.draw()
handle = Handle('на лбу')
handle.draw()