import random
M = int(input("M ="))
N = int(input("N ="))
a = []
katta_mas = []
for i in range(M):
    for j in range(N):
        z = random.randint(-5,9)
        a.append(z)
    katta_mas.append(a)
    print(a)
    a = []
kattasi = 0
index = 0
for k in range(len(katta_mas)):
    for l in range(len(katta_mas)):
        if kattasi < katta_mas[l][k]:
            kattasi = katta_mas[l][k]
            index = k
print(katta_mas)
for i in range(len(katta_mas)):
    for j in range(len(katta_mas)):
        nol = katta_mas[j][0]
        katta_mas[j][0] = katta_mas[j][index]
        katta_mas[j][index] = nol
print(katta_mas)