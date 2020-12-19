import json
avarage_profit={}
profit_list={}
count=0
profit=0
final_list=[]
with open("hw_5_7.txt","r") as fr:
    for line in fr:
        list_str=line.split(";")
        try:
            revenu=int(list_str[2])
            cost=int(list_str[3])
        except Exception as err:
            print(err)
        prof=revenu-cost
        profit_list[list_str[0]]=prof
        if prof>0:
            count+=1
            profit=profit+prof
    avarage_profit["avarage_profit"]=profit/count
final_list.append(profit_list)
final_list.append(avarage_profit)

with open("hw_5_7.json","w") as fw:
    json.dump(final_list,fw)