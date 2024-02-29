import random
M = int(input("M ="))
N = int(input("N ="))
mxn_katta = []
for i in range(M):
    mnx = []
    for j in range(N):
        z = random.randint(-5,5)
        mnx.append(z)
    print(mnx)
    mxn_katta.append(mnx)
sana  = 0
kichik_element = mxn_katta[0][0]
index = 0
elemet_joyi = 0
for  k in range(len(mxn_katta)):
    for l in range(len(mxn_katta)):
        if kichik_element > mxn_katta[k][l]:
            kichik_element = mxn_katta[k][l]
            index = k
            elemet_joyi = l
print("indedx =",index,"elemet_joyi =",elemet_joyi,"kichik_element =", kichik_element)
