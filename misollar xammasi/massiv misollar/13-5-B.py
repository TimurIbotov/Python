import random
N = int(input("N ="))
A = []
min = N
for i in range(N):
    z = random.randint(1,N)
    A.append(z)
    if min > z:
        min = z
print(min)
print(A)
