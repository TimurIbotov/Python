import random
M = int(input("M ="))
N = int(input("N ="))
a = []
X = []
for i in range(M):
    for j in range(N):
        z = random.randint(-5,5)
        a.append(z)
    print(a)
    X.append(a)
    a = []
print(X)
kicihik = 0
index = 0
joyi = 0
for k in range(len(X)):
    for l in range(len(X)):
        if kicihik < X[k][l]:
            kicihik = X[k][l]
            index = k
            joyi = l
print(index,kicihik)
X_n = X[0]
X[0] = X[index]
X[index] = X_n
print(X)