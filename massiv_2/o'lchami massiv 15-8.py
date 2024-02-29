'''import random
M = int(input("M ="))
N = int(input("N ="))
A = []
X = []
for i in range(M):
    for j in range(N):
        z = random.randint(1,9)
        A.append(z)
    # print(A)
    X.append(A)
    A = []
print(X)
for k in range(len(X)):
    if k == 0:
        l = max(X[0])
    else:
        if l < max(X[k]):
            l = max(X[k])
            b = 0
            c = 0
            b = X[k]
            c = X[0]
X[0] = b
X[k] = c

    
print(X)

# a=[[1,1],[2,2],[3,3],[4,4],[5,5]]
# b=0
# c=0
# b=a[1]
# c=a[0]
# a[0]=b
# a[1]=c
# print(a)'''
import random
M = int(input("M ="))
N = int(input("N ="))
A = []
X = []
for i in range(M):
    for j in range(N):
        z = random.randint(1,9)
        A.append(z)
    # print(A)
    X.append(A)
    A = []
print(X)

eng_katta = 0
eng_katta_index = 0
sana = 0
for k in X:
    print(k)
    for l in k:
        if eng_katta <= l:
            eng_katta = l
            eng_katta_index = sana
        print(eng_katta,sana)
    sana += 1
print(eng_katta,eng_katta_index)
print(X)
X_nol = X[0]
X[0]=X[eng_katta_index]
X[eng_katta_index] = X_nol
print(X)