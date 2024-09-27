import random
M = int(input("M ="))
N = int(input("N ="))
katta_mass = []
for i in range(M):
    kichik_mass = []
    for j in range(N):
        z = random.randint(1,20)
        kichik_mass.append(z)
    katta_mass.append(kichik_mass)    
    print(kichik_mass)
son = 20
ustun = 0
for i in range(M):
    index = 0
    for j in range(N):
        if son > katta_mass[j][i]:
            son = katta_mass[j][i]
            index += 1
    ustun += 1
print(katta_mass,'\n',"USTUN",ustun,"INDEX",index,"SON",son)