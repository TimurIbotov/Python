N = int(input("N ="))
V = 0
v1 = 0
v2 = 0
v3 = 1.5
for i in range(4,N+1):
    if N>=4:
        V = ((i + 1 )/ (i**2 + 1)) * v3 * v2 * v1
        v1 = v2
        v2 = v3
        v3 = V
    print(V)
else:
    print(v1,v2,v3)
    