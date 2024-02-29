import random
M = int(input("M = "))
N = int(input("N = "))
mnx = []
for i in range(M):
    m = 0
    for j in range(N):
        z = random.randint(1,5)
        mnx.append(z)
        if m < z:
            m = z
    mnx.append(m)
    print(mnx)
    mnx = []