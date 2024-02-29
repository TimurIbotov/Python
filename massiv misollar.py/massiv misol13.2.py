N = int(input("N ="))
i = 1
if N < 10:
    m = []
    while i <= N:
        m.append(i)
        i += 1
    print("M =", m)
else:
    print("10 dan katta bo'lmasligi kerak")