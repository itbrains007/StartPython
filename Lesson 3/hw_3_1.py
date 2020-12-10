#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def division (arg1, arg2):
    try:
        print(f"Деление a на b: {arg1/arg2}")
    except ZeroDivisionError:
        print("На ноль делить нельзя")
        return

a = input("Введите число a: ")
b = input("Введите число b: ")
try:
    a=float(a)
    b=float(b)
except Exception:
    print("Необходимо ввести число")
else:
    division(a,b)