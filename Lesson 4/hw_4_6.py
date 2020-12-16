from itertools import count,cycle
count_list=[]
for i in count(10):
    if i>20:
        break
    else:
        count_list.append(i)
print(count_list)

c=0
cycle_list = []
for j in cycle('qwerty'):
    if c > 15:
        break
    cycle_list.append(j)
    c += 1
print(cycle_list)
