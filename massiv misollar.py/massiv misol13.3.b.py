N = int(input("N ="))
if N > 1:
    u0 = 1
    u1=1
    U = 0
    a = []
    for i in range(2,N+1):
        U = u0 + u1
        u0 = u1
        u1 = U
        a.append(U)
    print(a)
    f0 = 0
    f1 = 1
    c = []
    F = 0
    for j in a:
        F = f1 + f0 + j
        f0 = f1
        f1 = F
        c.append(F)
    print(c)
    # M = [1 , 1]
    # f = [0, 1]
    # for j in range(0,N+1):
    #     b = len(M) 
    #     u = M[b-2] +  M[b-1]
    #     M.append(u)
    # for i in range(2, N+1):
    # #     F = f1 + f0 + u0
    # #     f0 = f1
    # #     u0 = f0
    # #     f1 = F
    #     h = len(f)
    #     F = f[h-1] + f[h-2] + M[i - 2] 
    #     f.append(F)
    # print(f)
else:
    print("1 dan katta bo'lishi kerak")