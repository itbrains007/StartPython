# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    a = [arg1, arg2, arg3]
    a.sort()
    print(a[1]+a[2])
    return

a = input("Введите число a: ")
b = input("Введите число b: ")
c = input("Введите число c: ")
try:
    a = float(a)
    b = float(b)
    c = float(c)
except Exception:
    print("Необходимо ввести число")
else:
    my_func(a, b, c)