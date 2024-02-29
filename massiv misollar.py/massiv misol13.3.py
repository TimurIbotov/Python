N = int(input("N ="))
M = [1,1]
u0=1
u1=1
for i in range(2,N):
    u = u1 + u0 
    u1 = u0
    u0 = u
    M.append(u)
print(M)