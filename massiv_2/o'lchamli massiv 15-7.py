import random
M = int(input("M ="))
N = int(input("N ="))
a = []
g = []
min = N
for i in range(M):
    for j in range(N):
        z = random.randint(1,N)
        a.append(z)
        if min > z:
            min = z
            x = j
    a.pop(x-1)
    print(a)
    a = []
    g.append(min)
    min = N
print(g)