N = int(input("N ="))
if N > 1:
    u0 = 1
    u1 = 1
    U = 0
    a = []
    for i in range(2,N+1):
        U = u1 + u0
        u0 = u1
        u1 = U
        a.append(U)
    print(a)
    f0 = 0
    f1 = 1
    F = 0
    c = []
    for j in a:
        F = f1 + f0 + j
        f0 = f1
        f1 = F
        c.append(F)
    print(c)