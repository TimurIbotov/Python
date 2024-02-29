N = int(input("N ="))
a = []
u0 = 1
u1 = 1
U = 0
for i in range(1,N+1):
    U = u1 + u0
    u0 = u1
    u1 = U
    a.append(U)
print(a)