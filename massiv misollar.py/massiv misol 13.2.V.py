N = int(input("N ="))
i = 1
P = 1
if N < 10:
    m = []
    while i <= N:
        P = P * i 
        m.append(P)
        i += 1
    print("M =", m)
else:
    print("10 dan katta bo'lmasligi kerak")