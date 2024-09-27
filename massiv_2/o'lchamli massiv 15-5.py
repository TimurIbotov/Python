import random
N = int(input("N ="))
M = int(input("M ="))
Katta_massiv = []
for i in range(N):
    a =[]
    for j in range(M):
        z = random.randint(1,N)
        a.append(z)
    print(a)
    Katta_massiv.append(a)
print(Katta_massiv)
# S = 1
# index = 0
# elemen = 0
# for k in range(len(Katta_massiv)):
#     for l in range(len(Katta_massiv)):
#         if Katta_massiv[k][l] >= S :
#             S = Katta_massiv[k][l]
#             index += 1
#     elemen =+ 1
#     print('elementi =',elemen,"indexsi =",index, "Son =",S)

s = 1
index1 = 0
element1 = 0
element = 0
for i in Katta_massiv:
    inex = 0
    for j in i :
        if j <= s:
            index1 = inex
            element = element1
        inex += 1
    element1 += 1
print("elementi =", element, "index =", index1 )