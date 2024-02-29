import random
N = int(input("N ="))
M = int(input("M ="))
L = int(input("L ="))
katta_mxn = []
for i in range(N):
    nxm = []
    for j in range(M):
        z = random.randint(1,4)
        nxm.append(z)
    print(nxm)
    katta_mxn.append(nxm)
katta_mxl = []
for k in range(M):
    mxl = []
    for l in range(L):
        a = random.randint(1,3)
        mxl.append(a)
    katta_mxl.append(mxl)
    print("\t",mxl)
P = 1
S = 0
for m in range(len(katta_mxl)):
    for b in range(len(katta_mxn)):
        S = katta_mxn[b][m] * katta_mxl[m][b] + S
    print(S)
print(katta_mxn,"\t",katta_mxl)