sum=0
with open("hw_5_5.txt","w") as fw:
    fw.write(input("Введите числа через пробел: "))

with open("hw_5_5.txt","r") as fr:
    try:
        text_str=fr.read()
        for i in text_str.split():
            sum=sum+int(i)
    except Exception as err:
        print(err)
print(sum)