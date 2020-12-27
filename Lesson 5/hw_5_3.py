d={}
with open("hw_5_3.txt","r") as fr:
    for line in fr:
        str=line.split(",")
        d[str[0]]=str[1]

sum=0
for i in d:
    if int(d[i])<20000:
        print(i, d[i])
    sum=sum+int(d[i])
print(sum / len(d))