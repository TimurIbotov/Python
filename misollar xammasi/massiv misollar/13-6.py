import random
N = int(input("N ="))
a = []
qadam = 0
for i in range(N):
    z = random.randint(1,N)
    a.append(z)
n = len(a)
print(a)
for k in range(n-1):
    for l in range(n-1):
        if a[l] > a[l+1]:
            a[l], a[l+1] = a[l+1], a[l]
            qadam += 1
print(a)
print(qadam)