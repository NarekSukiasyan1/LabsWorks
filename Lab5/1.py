def IsIllegalChar(ch):
    match ch:
        case '>':
            return True
        case '<':
            return True
        case '/':
            return True
        case '\\':
            return True
        case '|':
            return True
        case '?':
            return True
        case '*':
            return True
        case _:
            return False


def ReadExtension(str):
    match str:
        case "txt":
            return True
        case "docx":
            return True
        case "doc":
            return True
        case "odf":
            return True
        case "rtf":
            return True
        case _:
            return False


while (True):
    print("Введите строку\n")
    str = input()
    if str == "":
        break
    IsNorm = True
    for i in range(len(str)):
        it = IsIllegalChar(str[i])
        if it:
            print("Недопустимы символ")
            IsNorm = False
            break
        if str[i] == '.':
            if i > 0:
                if ReadExtension(str[i+1:]):
                    break
                else:
                    IsNorm = False
                    break
            else:
                IsNorm = False
                break
    if (IsNorm):
        print("Строка в норме")
    else:
        print("Строка не в норме")
