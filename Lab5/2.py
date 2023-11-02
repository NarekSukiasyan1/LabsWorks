import re

print("введите строку")
s = input()

if not s:
    print("Пустая строка")
else:
    s = re.sub(r"^\s+", "", s)
    s = re.sub(r"\s+$", "", s)

    s = s.lower()

    flag = re.search(r"[a-z]", s)
    if flag:
        s = re.sub(r"[a-z]", flag.group(0).upper(), s, 1)

    flag = re.search(r"[.!?]$", s)
    if flag:
        s = re.sub(r"[.!?]+$", "", s)
    s += "."
    print("ваша преобразованная строка")
    print(s)