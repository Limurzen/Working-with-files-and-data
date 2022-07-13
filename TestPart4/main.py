while True:
    inp = input("Введите команду «read», «copy» или «write»: ")
    if inp == "read":
        try:
            a = open("a.txt", "r")
            print(a.read())
            a.close()
        except FileNotFoundError:
            print("Файл покачто не создан")
    elif inp == "write":
        text = input("Введите текст который нужно добавить: ")
        a = open("a.txt", "w")
        a.write(text)
        a.close()
    elif inp == "copy":
        a = open("a.txt")
        b = open("b.txt", "w")
        for line in a:
            b.write(line)
        a.close()
        b.close()
