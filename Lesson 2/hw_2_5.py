#Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
my_list = [7, 5, 3, 3, 2]
number = input("Пожалуйста, ведите натуральное число:")
while number.isnumeric() == False :
    number = input("Жаль, это не натуральное число. Попробуй еще раз: ")
number=int(number)

try:
    position=my_list.index(number)
    count=my_list.count(number)
    my_list.insert(count+position, number)
    print(my_list)
except ValueError:
    my_list.append(number)
    my_list.sort(reverse=True)
    print(my_list)