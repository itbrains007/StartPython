#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
name_inp=input("Введите Имя: ")
surname_inp=input("Введите Фамилию: ")
bithday_inp=input("Введите дату рождения: ")
city_inp=input("Введите город проживания: ")
email_inp=input("Введите email: ")
phone_inp=input("Введите телефон: ")
def personal_info(name, surname, bithday, city, email, phone):
    all_info=''
    all_info=name+' '+surname+' '+bithday+' '+city+' '+email+' '+phone
    return all_info

print(personal_info(surname=surname_inp,name=name_inp,bithday=bithday_inp,city=city_inp,email=email_inp,phone=phone_inp))

