N = int(input("N ="))
S = 0
if N < 10:
    m = []
    for i in range(1, N+1):
        S = (2 ** i) + (3**(i+1))
        m.append(S)
    print("M =", m)
else:
    print("10 dan katta bo'lishi kerak")