import random
M = int(input("M ="))
N = int(input("N ="))
mas = []
katta_mass = []
for i in range(M):
    mxn = []
    for j in range(N):
        z = random.randint(1,5)
        mxn.append(z)
    print(mxn)
    katta_mass.append(mxn)
max = 0
for k in range(len(katta_mass)):
    max = 0
    for l in range(len(katta_mass)):
        if max < katta_mass[l][k] :
            max = katta_mass[l][k]
    mas.append(max)
print(mas)
        # print(katta_mass[l][k])
    # if max < katta_mass()