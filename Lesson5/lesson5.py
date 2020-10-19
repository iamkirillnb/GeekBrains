'''
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

with open('first_ex.txt', 'w', encoding='UTF-8') as first_ex:
    my_line = 'Введите строку:'
    while my_line != '':
        my_line = input('Введите строку: ')
        first_ex.write(my_line + '\n')

'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
'''
with open('second_ex.txt', 'r') as second_ex:
    rows = second_ex.readlines()
    print(f'Количество строк в файле {len(rows)}')
    for i in range(len(rows)):
        print(f'В {i+1} строке {len(rows[i].split())} слов')

'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
'''

person = {}
with open('third_ex.txt', 'r', encoding='UTF-8') as third_ex:
    for line in third_ex:
        key, value = line.split()
        person[key] = value
print('Выведем сотрудников с окладом меньше 20000р.')
for i,j in person.items():
    if int(j) < 20000:
        print(i, j)
#print([(i,j) for i, j in person.items() if int(j) < 20000])  Как бонус)
print(f'Средняя зарплата сотрудников: {sum(map(int, person.values())) / len(person)}р.')

'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''
rus_dict = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9}
sample = {}
with open('fours_input.txt', 'r', encoding='UTF-8') as fours_input:
    for i in fours_input:
        kay, value = i.split('—')
        sample[int(value)] = kay
for i, j in sample.items():
    for ii, jj in rus_dict.items():
        if i == jj:
            sample[i] = ii
with open('fours_output.txt', 'w', encoding='utf-8') as fours_out:
    for i, j in sample.items():
        fours_out.write(f'{j} - {i}\n')

'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
from random import randint
with open('fifth_ex.txt', 'w') as fifth_file:
    for i in range(10):
        fifth_file.write(f'{(randint(1, 20))} ')
with open('fifth_ex.txt', 'r') as numbers:
    a = numbers.read().split()
    print(f'Числа из файла: {a}')
    print(f'Сумма произвольных чисел из файла равна {sum(map(int, a))}')

'''
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
import re
sixth_dict = {}
with open('sixth.txt', 'r', encoding='UTF-8-sig') as sixth_file:
    for i in sixth_file:
        key, *value = i.split()
        sixth_dict[key] = [re.match(r'(\d*)', j).group() for j in value]
for i, j in sixth_dict.items():
    value = [int(x) for x in j if x]
    sixth_dict[i] = sum(value)
print(sixth_dict)

'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''
import json
seventh_dict1 = {}
seventh_dict2 = {}
avrg = {}
with open('seventh.txt', 'r', encoding='UTF-8-sig') as seevnth_file:
    for i in seevnth_file:
        key, *value = i.split()
        value = list(map(int, value[1:]))
        profit = value[0] - value[-1]
        seventh_dict2[key] = profit
        if profit > 0:
            seventh_dict1[key] = profit
    seventh_dict1['average_profit'] = sum(seventh_dict1.values())/len(seventh_dict1)
    avrg['average_profit'] = sum(seventh_dict2.values()) / len(seventh_dict2)
print(f'Выводим словарь по первому подзаданию: {seventh_dict1}')
print(f'Выводим список по второму подзаданию: {[seventh_dict2, avrg]}')
out_list = [seventh_dict2, avrg]
with open('seventh_output.json', 'w', encoding='UTF-8') as seventh_output:
    json.dump(out_list, seventh_output, ensure_ascii=False)

