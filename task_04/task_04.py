# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
number = int(input("Введите число: "))
i = 0
double_number = 0
while number > 0:
    double_number = double_number + (number % 2) * 10 ** i
    number = number // 2
    i = i + 1
print(double_number)