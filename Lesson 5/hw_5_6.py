d={}
num_str=''
with open("hw_5_6.txt","r") as fr:
    for line in fr:
        sum_all = 0
        list_str=line.split(":")
        for i in list_str[1]:
            if i.isdigit():
                num_str=num_str+i
            else:
                if num_str != '':
                    sum_all = sum_all + int(num_str)
                    num_str=''
        d[list_str[0]]=sum_all
print(d)