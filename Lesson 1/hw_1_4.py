#Lesson_1_4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
n = input("Пожалуйста, ведите натуральное число:")
i=0
maximum=1
while n.isnumeric() == False:
    n = input("Жаль, это не натуральное число. Попробуй еще раз:")
else:
    while i < len(n):
        if int(n[i]) > maximum:
            maximum=int(n[i])
        i = i + 1
    print(f"А вот и максимум: {maximum}")