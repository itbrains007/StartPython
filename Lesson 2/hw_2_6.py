#Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
i=0
input_yes='yes'
list_goods=[]
name_list=[]
price_list=[]
count_list=[]
unit_list=[]
while input_yes=='yes':
    name = input("Введите название товара: ")
    price = input("Введите цену товара: ")
    count = input("Введите количество товара: ")
    unit = input("Введите единицу измерения товара: ")
    i=i+1
    list_goods.append((i,{"название":name,"цена":price, "количество":count, "ед":unit}))
    input_yes=input("Продолжаем вводить товар (yes/no): ")
for j in list_goods:
    list_val=j[1].values()
    analys_dict = zip(name_list,list_val)
    name_list.append(j[1].get("название"))
    price_list.append(j[1].get("цена"))
    count_list.append(j[1].get("количество"))
    unit_list.append(j[1].get("ед"))
analys_dict={'название':list(set(name_list)),'цена':list(set(price_list)),'количество':list(set(count_list)),'eд':list(set(unit_list)) }
print(analys_dict)