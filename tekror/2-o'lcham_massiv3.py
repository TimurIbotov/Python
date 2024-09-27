import random
M = int(input("M ="))
N = int(input("N ="))
for i in range(M):
    a = []
    aa = 0
    for j in range(N):
        z = random.randint(1,9)
        a.append(z)
        if aa < z  :
            aa = z
    a.append(aa)
    print(a)