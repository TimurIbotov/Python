import random
M = int(input("M ="))
N = int(input("N ="))
massiv_k = []
for i in range(M):
    a = []
    for j in range(N):
        z = random.randint(1,50)
        a.append(z)
    massiv_k.append(a)
print(massiv_k)
katta_raqamlar_mass = []
for l in range(M):
    raqam = 0
    for m in range(N):
        if raqam < massiv_k[m][l]:
            raqam = massiv_k[m][l]
    katta_raqamlar_mass.append(raqam)
massiv_k.append(katta_raqamlar_mass)
print('------------>',massiv_k)
        # print(massiv_k[m][l])