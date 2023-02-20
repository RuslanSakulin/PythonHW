# Задача 2: Найдите сумму цифр трехзначного числа.
num = int(input("Введите число: "))
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
 
print("Сумма:", sum)