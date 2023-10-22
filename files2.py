with open("hello.txt", "r") as file:
    print(file.tell())
    file.seek(3)
    print(file.tell())
