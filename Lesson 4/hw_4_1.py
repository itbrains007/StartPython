from sys import argv

script_name, working_time, price, bonus = argv
try:
    working_time = int(working_time)
    price = int(price)
    bonus = int(bonus)
except Exception as err:
    print("Somethink wrong", err)
salary=(working_time*price)+bonus
print("Our salary: ", salary)