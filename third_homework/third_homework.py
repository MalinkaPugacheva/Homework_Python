# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

x = [2, 3, 6, 10, 12, 16, 5]
#print(x)
summ = 0
for i in range(1, len(x), 2):
    #if i % 2 == 1:
        summ += x[i]       
print(f"{x} -> сумма элементов на нечётных позициях: {summ}")

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint


number = int(input('Введите размер списка '))
list = []
list2 = []

for i in range(number):
    list.append(randint(0, 9))

for i in range(len(list)):
    while i < len(list)/2 and number > len(list)/2:
        number = number - 1
        a = list[i] * list[number]
        list2.append(a)
        i += 1

print(list)
print(list2)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform


n = int(input('Введите размер списка '))
list1 = []
for i in range(n):
    f = uniform(0, 9)
    list1.append(round(f, 2))

min = list1[0]
max = 0
for i in range(len(list1)):
    
    if max < list1[i]:
        max = list1[i]
    if min > list1[i]:
        min = list1[i]
dif = (max - int(max)) - (min - int(min))

print(list1)
print(max, min)
print(round(dif,2))

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# a = int(input())
# f = bin(a)
# print(f)


a = int(input('Введите число '))
b = ''
while a > 0:
    b = str(a%2) + b
    a = a // 2
print(b)

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


n = int(input('Введите размер числа Фибоначчи '))
if n < 0: n = n*-1
f1 = f2 = 1
list1 = [f1, f2]
for i in range(2, n):
    f1,f2 = f2, f1 + f2
    list1.append(f2)
print(list1)
f1=f2=1
for i in range(-n, 1):
    f1,f2 = f2, f1 - f2
    list1.insert(0, f2)
print(list1)

