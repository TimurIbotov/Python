import random
N = int(input("N ="))
a = []
for i in range(N):
    z = random.randint(1,N)
    a.append(z)
max = a[0]
k = 1
for j in a:
    k += 1
    if k % 2 == 0:
        print(j)
        if max < j:
            max = j
print(a)
print(max)