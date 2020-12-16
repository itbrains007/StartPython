from functools import reduce

def multi(arg1, arg2):
    return arg1 * arg2

my_list=[i for i in range(100, 1001, 2)]
print(reduce(multi,my_list))