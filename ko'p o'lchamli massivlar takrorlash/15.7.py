import random
M = int(input("M ="))
N = int(input("N ="))
mxn_katta_massiv = []
for i in range(M):
    mxn = []
    for j in range(N):
        z = random.randint(-5,5)
        mxn.append(z)
    print(mxn)
    mxn_katta_massiv.append(mxn)
print(mxn_katta_massiv)
min_element = mxn_katta_massiv[0][0]
index = 0
element = 0
for i in range(len(mxn_katta_massiv)):
    for j in range(len(mxn_katta_massiv)):
        if min_element > mxn_katta_massiv[i][j]:
            min_element = mxn_katta_massiv[i][j]
            index = i
            element = j
print("index =",index,"element =",element,"min_element =",min_element)
mxn_katta_massiv.pop(index)
print(index)
print(mxn_katta_massiv)