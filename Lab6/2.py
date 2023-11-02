import re
matrix = [[[],[]],[[],[]]]
for i in range(2):
    print("Введите кол-во строк и столбцов матрицы номер ", i, " через пробел")
    str =input()
    str = re.sub(r"\s",'',str)
    a,b
    if str.isdigit():
        a = int(str)//10
        b = int(str)//10
    for j in range(a):
        print