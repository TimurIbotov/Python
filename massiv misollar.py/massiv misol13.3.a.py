N = int(input("N ="))
u0=1
u1=1
if N>1:
    M = [1,1]
    for i in range(0,N+1):
        # u = u1 + u0 
        # u1 = u0
        # u0 = u
        b = len(M) 
        u = M[b-2] +  M[b-1]
        M.append(u)

    print(M)
else:
    print("1 dan katta bo'lishi kerak")