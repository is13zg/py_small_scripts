# решение примеров

n = 15
Answer_Only = 1
DIV = 1
Numeration = 1

for i in range(1, n + 1):
    s = input()
    s2 = s.replace(' ', "")
    s2 = s2.replace('=', "")
    s2 = s2.replace('х', "*")
    s2 = s2.replace('•', "*")
    s2 = s2.replace('·', "*")
    s2 = s2.replace('x', "*")
    s2 = s2.replace('Х', "*")
    s2 = s2.replace('×', "*")
    s2 = s2.replace('—', "-")
    s2 = s2.replace('–', "-")
    if DIV:
        s2 = s2.replace("÷", '//')
        s2 = s2.replace(":", '//')
    else:
        s2 = s2.replace("÷", '/')
        s2 = s2.replace(":", '/')

    if Numeration:
        if Answer_Only:
            print(str(i) + ".", eval(s2), end="; ")
        else:
            print(str(i) + ".", s, "=", eval(s2))
    else:
        if Answer_Only:
            print(eval(s2), end="; ")
        else:
            print(s, "=", eval(s2))
