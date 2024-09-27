import random
M = int(input("M ="))
N = int(input("N ="))
mxn = []
katta_mxn_Mass = []
for i in range(M):
    for j in range(N):
        z = random.randint(-5,5)
        mxn.append(z)
    print(mxn)
    katta_mxn_Mass.append(mxn)
    mxn = []
sana = 0
index = 0
eng_kichik = 5
for k in range(len(katta_mxn_Mass)):
    for l in range(len(katta_mxn_Mass)):
        if eng_kichik > katta_mxn_Mass[l][k]:
            eng_kichik = katta_mxn_Mass[l][k]
            index = sana
    sana += 1
    print(eng_kichik,index)
for m in range(len(katta_mxn_Mass)):
    # if katta_mxn_Mass[m]
    # print(katta_mxn_Mass[m][index])
    katta_mxn_Mass[m].pop(index)
print(katta_mxn_Mass)