import re

print("введите строку")
s1 = input()

print("введите подстроку")
s2 = input()

flag = re.findall(s2, s1)

if not flag:
    print("вхождений не найдено")
else:
    res = re.sub(s2, "", s1, len(flag)-1)
    print("ваша измененная строка")
    print(res)