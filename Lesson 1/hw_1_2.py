#Lession 1_2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
second = input("Пожалуйста, ведите количество секунд:")
while second.isnumeric() == False:
    second = input("Жаль, это не натуральное число. Попробуй еще раз:")
else:
    second=int(second)
while second >= 86400:
    second = int(input("Ну очень большое число. Попробуй еще раз:"))
else:
    hour = second//3600
    min = (second-hour*3600)//60
    sec = second%60
    print(f"Вермя:{hour:02}:{min:02}:{sec:02}")