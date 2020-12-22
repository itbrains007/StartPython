d={"One":"Один", "Two":"Два", "Three":"Три", "Four":"Четыре"}
with open("hw_5_4_new.txt","w") as fw:
    with open("hw_5_4.txt","r") as fr:
        for line in fr:
            slist=line.split()
            slist[0]=d[slist[0]]
            fw.write(" ".join(slist)+"\n")