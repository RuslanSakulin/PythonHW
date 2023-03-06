# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input('Input number of elements: '))
lst = [int(input('Input elements of list: ')) for i in range(n)]
print(lst)
x = int(input('Input the desire number: '))
print(f'The nuber {x} occurs {lst.count(x)} times in the list. ')