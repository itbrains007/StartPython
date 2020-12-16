def fact (n):
    multi = 1
    for el in range(1,n+1):
        multi = multi*el
        yield multi

num = input("Введите число для нахождения факториала: ")
try:
    num=int(num)
except Exception as err:
    print(err)
else:
    factor=fact(num)
    for j in range(num):
        print(next(factor))
