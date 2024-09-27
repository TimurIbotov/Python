import random
M = int(input("M ="))
N = int(input("N ="))
katta_massiv = []
for i in range(M):
    a = []
    for j in range(N):
        z = random.randint(1,20)
        a.append(z)
    katta_massiv.append(a)
# print(katta_massiv)
massiv_elementi = 0
for k in range(M):
    kichi_raqam = 20
    massiv_elementini_indexsi = 0
    for l in range(N):
        # print(katta_massiv[k][l])
        if kichi_raqam > katta_massiv[k][l]:
            kichi_raqam = katta_massiv[k][l]
            massiv_elementini_indexsi += 1
    massiv_elementi += 1
print(katta_massiv,'\n','index',massiv_elementi,'indexsinig',massiv_elementini_indexsi,'kichik raqami ->',kichi_raqam)
