import random
M = int(input("M ="))
N = int(input("N ="))
for i in range(M):
    mnx =[]
    katta_son = -5
    for j in range(N):
        z = random.randint(-5,5)
        mnx.append(z)
        if katta_son < z :
            katta_son = z
    mnx.append(katta_son)
    print(mnx)