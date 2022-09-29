# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

n = int(input("Введите размер массива: "))
array = []
for i in range(n):
    array.append(round(random.uniform(0, 10), 3))
print(array)
min = round(array[0] % 1, 3)
max = round(array[0] % 1, 3)
for i in range(n):
    if round(array[i] % 1, 3) < min:
        min = round(array[i] % 1, 3)
    else:
        if round(array[i] % 1, 3) > max:
            max = round(array[i] % 1, 3)

print(f'Разница: ', max - min)