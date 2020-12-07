# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
month_inp = input("Введите месяц: ")
while month_inp.isnumeric() == False:
    month_inp = input("Должно быть число от 1 до 12. Попробуйте еще раз: ")
else:
    month = int(month_inp)
    if month < 1 or month > 12:
        month = input("Должно быть число от 1 до 12. Попробуйте еще раз: ")

year_dict = {1: 'Winter',
             2: 'Winter',
             3: 'Spring',
             4: 'Spring',
             5: 'Spring',
             6: 'Summer',
             7: 'Summer',
             8: 'Summer',
             9: 'Autumn',
             10: 'Autumn',
             11: 'Autumn',
             12: 'Winter', }
print(year_dict.get(month))

year_list=['Winter','Winter','Spring','Spring','Spring','Summer','Summer','Summer','Autumn','Autumn','Autumn','Winter']
print(year_list[month-1])

