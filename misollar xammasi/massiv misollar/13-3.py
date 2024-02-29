N = int(input("N ="))
a = []
u0 = 1
u1 = 1
U = 0
for i in range(2,N+1):
    U = u1 + u0
    u0 = u1
    u1 = U
print(U)