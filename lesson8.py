'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''

'''class MyData:
    def __init__(self, my_time):
        self.my_time = my_time

    def __str__(self):
        return self.my_time         #f'{self.my_time}'

    @classmethod
    def decor(cls, my_data):
        day, month, year = list(map(int, my_data.split('-')))
        return day, month, year

    @staticmethod
    def check_date(*args):
        days = {31: (1, 3, 5, 7, 8, 10, 12), 28: (2,), 30: (4, 6, 9, 11)}
        for i, j in days.items():
            if month in j and 1 <= day <= i:
                return f'Correct date'
        else:
            return f'Not correct date'


data1 = '01-01-2020'
a = MyData(data1)
print(a)
day, month, year = a.decor(data1)
print(MyData.check_date(day, month, year))'''

'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. 
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''

"""class MyDevevizionByZero(Exception):
    def __init__(self, text):
        self.text = text

def my_div(a, b):
    print('Деление A на B:')
    while True:
        try:
            print(f'a = {a}')
            b = int(input('Введите значение b: '))
            if b == 0:
                raise MyDevevizionByZero('Мое деление на ноль запрещено!')
        except MyDevevizionByZero as my_err:
            print(f'{my_err} ПОНЯТНО?\nПробуй еще раз')
        else:
            return round(a / b, 2)


print(my_div(5,0))"""


'''
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
'''


'''class CheckListError(Exception):
    def __init__(self, text):
        self.text = text


def check_list_func():
    my_list = []
    while True:
        try:
            number = input('Введите значение: ')
            if not number.isdigit() and number != 'stop':
                raise CheckListError('Список должен состоять только из чисел!')
            elif number == 'stop':
                return my_list
            else:
                my_list.append(int(number))
        except CheckListError as my_err:
            print(my_err)


print(check_list_func())'''

'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. 
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
'''
from abc import ABC, abstractmethod

class Warehouse(ABC):
    pass

    @abstractmethod
    def counter(self):
        pass





class OfficeEquipWarehouse(Warehouse):
    cnt = 0
    def __init__(self, brand, price, color, height=0, width=0, length=0):
        self.brand = brand
        self.price = price
        self.color = color
        self.height = height
        self.width = width
        self.length = length
        OfficeEquipWarehouse.cnt += 1


    @abstractmethod
    def what_quality(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @staticmethod
    def count_all(name):
        office_dict = {}
        office_dict[name.__name__] = f'{name.cnt} вещи'
        return office_dict



class Printer(OfficeEquipWarehouse):
    printer_dict = {}
    cnt = 0
    quality = {
        'Panasonic': '★',
        'Samsung': '★★',
        'Toshiba': '★★★',
        'Epson': '★★★★',
        'Konica Minolta': '★★★★★',
        'Kyocera': '★★★★★★',
        'Canon': '★★★★★★★',
        'Hewlett Packard': '★★★★★★★★',
        'Xerox': '★★★★★★★★★',
    }

    def __init__(self, brand, price, color, height, width, length, printing_technology):
        super().__init__(brand, price, color, height, width, length)
        self.printing_technology = printing_technology
        Printer.cnt += 1
        Printer.printer_dict.setdefault(self.brand, []).append(1)



    def __str__(self):
        return f'Марка={self.brand}\nЦена={self.price}\nЦвет={self.color}\nВысота={self.height}\nШирина={self.width}\nДлина={self.length}\nТип устройства={self.printing_technology}'


    def what_quality(self):
        for i, j in Printer.quality.items():
            if self.brand == i:
                return f'Качество {self.brand} ({Printer.__name__}) {j}'

    def __del__(self):
        Printer.cnt -= 1
        OfficeEquipWarehouse.cnt -= 1
        del self

    def size(self):
        return f'Габариты {self.brand} ({Printer.__name__}):\nВысота = {self.width}см Ширина = {self.height}см Длина = {self.length}см\n'

    @property
    def counter(self):
        for i, j in Printer.printer_dict.items():
            if i == self.brand:
                Printer.printer_dict[i] = j
        return Printer.printer_dict



class Scaner(OfficeEquipWarehouse):
    scaner_dict = {}
    cnt = 0
    quality = {
        'Fujitsu': '★',
        'Brother': '★★',
        'Hewlett Packard': '★★★',
        'Kodak': '★★★★',
        'Epson': '★★★★★',
        'Canon': '★★★★★★',
    }
    def __init__(self, brand, price, color, height, width, length, type_of_scanner):
        super().__init__(brand, price, color, height, width, length)
        self.type_of_scanner = type_of_scanner
        Scaner.cnt += 1
        Scaner.scaner_dict.setdefault(self.brand, []).append(1)

    def __str__(self):
        return f'Марка={self.brand}\nЦена={self.price}\nЦвет={self.color}\nВысота={self.height}\nШирина={self.width}\nДлина={self.length}\nТип устройства={self.type_of_scanner}'

    def what_quality(self):
        for i, j in Scaner.quality.items():
            if self.brand == i:
                return f'Качество бренда {self.brand} ({Scaner.__name__}) {j}'

    def __del__(self):
        Scaner.cnt -= 1
        OfficeEquipWarehouse.cnt -= 1
        del self



    def size(self):
        return f'Габариты {self.brand} ({Scaner.__name__}):\nВысота = {self.width}см Ширина = {self.height}см Длина = {self.length}см\n'

    @property
    def counter(self):
        for i, j in Scaner.scaner_dict.items():
            if i == self.brand:
                Scaner.scaner_dict[i] = j
        return Scaner.scaner_dict

class Xerox(OfficeEquipWarehouse):
    xerox_dict = {}
    cnt = 0
    quality = {
        'Brother': '★',
        'Xerox': '★★',
        'Pantum': '★★★',
        'Hewlett Packard': '★★★★',
        'Canon': '★★★★★',
        'Epson': '★★★★★★',
    }

    def __init__(self, brand, price, color, height, width, length, resolution):
        super().__init__(brand, price, color, height, width, length)
        self.resolution = resolution
        Xerox.cnt += 1
        Xerox.xerox_dict.setdefault(self.brand, []).append(1)

    def __str__(self):
        return f'Марка={self.brand}\nЦена={self.price}\nЦвет={self.color}\nВысота={self.height}\nШирина={self.width}\nДлина={self.length}\nТип устройства={self.resolution}'

    def what_quality(self):
        for i, j in Xerox.quality.items():
            if self.brand == i:
                return f'Качество {self.brand} ({Xerox.__name__}) {j}'


    def __del__(self):
        Xerox.cnt -= 1
        OfficeEquipWarehouse.cnt -= 1
        del self


    def size(self):
        return f'Габариты {self.brand} ({Xerox.__name__}):\nВысота = {self.width}см Ширина = {self.height}см Длина = {self.length}см\n'

    @property
    def counter(self):
        for i, j in Xerox.xerox_dict.items():
            if i == self.brand:
                Xerox.xerox_dict[i] = j
        return Xerox.xerox_dict




print(OfficeEquipWarehouse.count_all(OfficeEquipWarehouse))
print()
printer1 = Printer('Xerox', 15000, 'black', 10, 10, 10, 'струйный')
print(Printer.count_all(Printer))
print(printer1)
print()
print(OfficeEquipWarehouse.count_all(OfficeEquipWarehouse))
print()
print(printer1.what_quality())
print(printer1.size())
printer2 = Printer('Samsung', 11000, 'gray', 12, 10, 24, 'лазерный')
printer3 = Printer('Samsung', 11000, 'gray', 12, 10, 24, 'лазерный')
print(Printer.count_all(Printer))
print(printer2.what_quality())
print(printer2.size())
print()

scaner1 = Scaner('Brother', 11000, 'yellow', 20, 15, 30, 'рулонный')

del printer3
print(OfficeEquipWarehouse.count_all(OfficeEquipWarehouse))
print(Printer.count_all(Printer))
print(Scaner.count_all(Scaner))
print(Xerox.count_all(Xerox))



'''
7. Реализовать проект «Операции с комплексными числами». 
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. 
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
'''

'''class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{complex(self.a, self.b)}'

    def __add__(self, other):
        return complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return complex((self.a * other.a) - (self.b * other.b), (self.a * other.b) + (other.a * self.b))


first = ComplexNumber(1,2)
print(first)

second = ComplexNumber(3,4)
print(second)
print(f'Сложение = {first + second}')
print(f'Умножение = {first * second}')'''

