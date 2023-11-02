import re

print("введите строку")
s = input()

if re.match(r"[a-zA-Z]{2}\d{3}[a-zA-Z]", s):
    print("Это номер")
else:
    print("Это не номер")