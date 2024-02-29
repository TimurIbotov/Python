import random
N = int(input("N ="))
a = []
for i in range(N):
    z = random.randint(1,N)
    a.append(z)
max = a[0]
k = 0
for j in a:
    k += 1
    if k % 2 == 0:
        if max > j:
            max = j
print(a)
print(max)