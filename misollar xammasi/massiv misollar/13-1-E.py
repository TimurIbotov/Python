import random
N = int(input("N ="))
a = []
S = 0
P = 1
for i in range(N):
    z = random.randint(1,N)
    a.append(z)
    S = S + z
    P = P * z
print(a)
print(S)
print(P)