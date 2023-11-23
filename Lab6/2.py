import re
import string

matrix = []
for i in range(2):
    print("Введите кол-во строк и столбцов матрицы номер ", i+1, " через пробел")
    str = input()
    str = str.split(' ')
    a = 0
    b = 0
    for j in range(2):
        try:
            c = int(str[j])
        except:
            print("Error")
            exit()
    j = 0
    a = int(str[0])
    b = int(str[1])
    matrix.append([[0 for i in range(b)] for j in range(a)])
    print("Введите матрицу построчно")
    for x in range(a):
        print("Введите ", b, " элементов ", x+1, "строки через пробел")
        str = input()
        str = str.split(' ')
        for y in range(b):
            try:
                matrix[i][x][y] = int(str[y])
            except:
                print("Введено не число")
                exit()
a = len(matrix[0][0])
b = len(matrix[1])
if (a != b):
    print("Матрицы неподходящих размеров")
    exit
a = len(matrix[0])
b = len(matrix[1][0])
result = []
for i in range(a):
    result.append([0 for j in range(b)])
for i in range(b):
    for j in range(a):
        result[i][j] = 0
        for k in range(len(matrix[0][0])):
            result[i][j] += matrix[0][i][k] * matrix[1][k][j]
    print("\n")
for i in range(b):
    for j in range(a):
        print(result[i][j], end =' ')
    print()
