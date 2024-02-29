import random
N = int(input("N ="))
a = []
z = 0
S = z / 1
P = 1
for i in range(1,N+1):
    z = random.randint(1,N)
    a.append(z)
    P = P * i
    S = (z / P) + S
print(a)
print(S)