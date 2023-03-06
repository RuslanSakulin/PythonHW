# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. .
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint
n = int(input('Input number of elements: '))
x = int(input('Input the number: '))
lst = [randint(1, 99) for i in range(n)]
nearest = min(lst, key = lambda i:abs(i - x))
print(lst)
print(f'{nearest} is the nearest number to {x}')
