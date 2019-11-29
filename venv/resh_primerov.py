import sys

data = list(map(str.strip, sys.stdin))
for ex in data:
    try:
        m1 = int(ex.split("X")[0])
        res = int(ex.split("=")[1].split("(")[0])
        m2 = res // m1
        m2r = res / m1
        if abs(m2r - m2) > 0:
            print("Error", ex)
        else:
            print(ex.replace("_", str(m2)))
    except:
        print("EX  Error", ex)
