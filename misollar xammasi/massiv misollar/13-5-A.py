import random
N = int(input("N ="))
A = []
max = 0
for i in range(N):
    z = random.randint(1,10)
    A.append(z)
    if max < z:
        max = z
print(A)
print(max)