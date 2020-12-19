with open("my_new_file.txt","w") as f:
    instr = input("Введите строку: ")
    while instr != "":
        f.writelines(instr + "\n")
        instr = input("Введите строку: ")
