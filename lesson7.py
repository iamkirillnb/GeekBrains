'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
'''

class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join([' '.join([str(self.lists[i][j]) for j in range(len(self.lists[i]))]) for i in range(len(self.lists))])

    def __add__(self, other):
        for i in range(len(self.lists)):
            for j in range(len(self.lists)):
                self.lists[i][j] = self.lists[i][j] + other.lists[i][j]
        return self.__str__()


example1 = [[1, 2, 3], [5, 3, 2], [9, 0, 6]]
example2 = [[5, 3, 1], [2, 1, 5], [7, 5, 2]]
matrix1 = Matrix(example1)
matrix2 = Matrix(example2)
print(f'Первая матрица\n{matrix1}')
print(f'Вторая матрица\n{matrix2}')
print(f'Сумма двух матриц\n{matrix1+matrix2}')

'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). 
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def coast(self):
        pass

    @staticmethod
    def summa(*args):
        cnt = 0
        for j in args:
            cnt += j
        return f'Общий расход ткани составляет {cnt}'


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def coast(self):
        return int(self.v / 6.5 + 0.5)

class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def coast(self):
        return int(2 * self.h + 0.3)


my_coat = Coat(180)
my_suit = Suit(180)
print(f'Расход ткани на пальто составляет {my_coat.coast}')
print(f'Расход ткани на костюм составляет {my_suit.coast}')
print(Clothes.summa(my_suit.coast, my_coat.coast))



'''
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__())
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное 
(не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
'''

class Cell:
    def __init__(self, cnt):
        self.cnt = cnt

    def __str__(self):
        return f'{self.cnt}'

    def __add__(self, other):
        return self.cnt + other.cnt

    def __sub__(self, other):
        if self.cnt < other.cnt:
            return f'Получается отирцательное значение!'
        return self.cnt - other.cnt

    def __mul__(self, other):
        return self.cnt * other.cnt

    def __truediv__(self, other):
        return int(self.cnt / other.cnt)

    def make_order(self, in_row):
        my_list = []
        for i in range(self.cnt // in_row):
            my_list.append("*" * in_row)
            my_list.append('\\n')
        my_list.append("*" * (self.cnt % in_row))
        return ''.join(my_list)


first = Cell(9)
second = Cell(7)
print(first)
print(second)
print(first*second)
print(first.make_order(4))
print(second.make_order(3))