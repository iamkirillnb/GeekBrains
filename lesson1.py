
#Первая задача
one = 1
two = 'two'
three_one = 3.1
print(f'{one}, {two}, {three_one}')
number_input = int(input('Введите цифру: '))
text_input = input('Введите текст: ')
print(f'{number_input}, {text_input}')

# Вторая задача
time = int(input('Введите количество секунд(0..86399): '))
hour = time // 3600
minute = (time % 3600) // 60
second = time % 60
import datetime
time_view = datetime.time(hour=hour, minute=minute, second=second)
print(f'Точное время {time_view}')

#Тртья задача
n = input('Введите число "n": ')
print(int(n) + int(n+n) + int(n+n+n))

# Четвертая задача
number = int(input('Введите число: '))
maxi = 0
last = 0
while number > 0:
    last = number % 10
    if last > maxi:
        maxi = last
    number = number // 10
print(maxi)

# Пятая задача
revenue = float(input('Введите значение выручки: '))
expenses = float(input('Введите значение издержек: '))
if revenue > expenses:
    print('Фирма работает в прибыль.')
    profit = revenue - expenses
    print(f'Рентабельность = {round(profit/revenue,4) * 100} %')
    employed = int(input('Введите количество сотрудников фирмы: '))
    print(f'На одного трудящегося приходится {round(profit/employed, 2)} руб.')

elif revenue < expenses:
    print('Фирма работает в убыток.')
else:
    print('Компания работает в ноль.')

#Шестая задача
a = 2
b = 3
count = 0
while True:
    count += 1
    print('%d-й день: %.2f км' % (count, a))
    a = a + (a * 10) / 100
    if a > b:
        print('Ответ: %d-й день | %.2f км' % (count+1, a))
        break

