# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# F_{0}=0, F_{1}=1, F_{n}=F_{n-1} + F_{n-2}}

def fibonaccio(n):
    if n < 0:
        return fibonaccio(n + 2) - fibonaccio(n + 1)
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaccio(n - 1) + fibonaccio(n - 2)

number = int(input("Введите число: "))
array = []
count = 0
for i in range(-number, number + 1):
    array.append(fibonaccio(i))
    count += 1

print(array)