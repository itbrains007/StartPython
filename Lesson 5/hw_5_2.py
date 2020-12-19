i = 0
with open("hw_5_2.txt","r") as fr:
    for line in fr:
        i += 1
        print(line, i, line.count(" ")+1)
