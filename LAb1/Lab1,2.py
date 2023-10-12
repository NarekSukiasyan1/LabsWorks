dic = {}
for i in range(3):
    print("Введите имя сотрудника")
    name = input()
    print("Введите оклад")
    i = int(input())
    i2 = i + i * 2 / 3
    salary = round(0.83 * i2, 2)
    dic[name] = salary
for i in dic:
    print(i,':', dic[i])