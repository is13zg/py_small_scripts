Kol= 15
Numeration = 1
N = 15
res = 0
for i in range(1, Kol + 1):
    d = int(input())
    if Numeration:
        if d % N == 0:
            if res:
                print(str(i) + ".", d//N,end="; ")
            else:
                print(str(i) + ".", d, end="; ")
    else:
        if d % N == 0:
            if res:
                print(d//N,end="; ")
            else:
                print(d, end="; ")