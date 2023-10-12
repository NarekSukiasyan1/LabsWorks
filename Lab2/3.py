a = int(input("Введите число"))
for i in range(9):
    for j in range(10):
        for z in range(10):
            if ((i+1)+j+z == a):
                print(i+1, j, z)
