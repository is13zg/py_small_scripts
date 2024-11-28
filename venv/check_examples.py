# решение примеров

n = 150
Answer_Only = 1
DIV = 0
DIV_if_possible = 1
Numeration = 1
Otveti_v_stolbik = 1


def safe_eval_decorator(func):
    def wrapper(expression):
        try:
            result = func(expression)
            if DIV_if_possible:
                if result == round(result):
                    return round(result)
                else:
                    return result
        except Exception as e:
            print(f"Ошибка: {e}")
            return None
    return wrapper

eval = safe_eval_decorator(eval)


for i in range(1, n + 1):
    s = input()
    if "." in s:
        s = s.split(".")[1]
        s= s.strip()
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
    s2 = s2.replace('−', "-")
    s2 = s2.replace(',', ".")
    if DIV:
        s2 = s2.replace("÷", '//')
        s2 = s2.replace(":", '//')
    else:
        s2 = s2.replace("÷", '/')
        s2 = s2.replace(":", '/')

    if Otveti_v_stolbik:
        sss = "\n"
    else:
        sss = "; "

    if Numeration:
        if Answer_Only:
            print(str(i) + ".", eval(s2), end=sss)
        else:
            print(str(i) + ".", s, "=", eval(s2))
    else:
        if Answer_Only:
            print(eval(s2), end=sss)
        else:
            print(s, "=", eval(s2))
