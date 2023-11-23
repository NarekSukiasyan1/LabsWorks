import re

while True:
    print("введите строку")
    s = input()

    if not s:
        print("конец программы")
        break
    else:
        if re.match(r"[^\\<>/|?*\"]+\.(txt|doc|docx|odt|rtf)", s):
            print(s, " - является названием файла")