# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

s = int(input("Введите общее количество журавликов: "))
a = (s / 6) * 4
b = a / 4
print (f"Если ребята сделали ({s}) журавликов, то Катя сделала ({int(a)}) журавликов, а Петя и Сережа по ({int(b)}) журавликов.")