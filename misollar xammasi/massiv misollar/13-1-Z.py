import random
N = int(input("N ="))
a = []
S = 0
P = 1
for i in range(N):
    z = random.randint(1,N)
    a.append(z)
    P = P * i
    S = (((-1)**i)*z)/P + S
print(a)
print(S)