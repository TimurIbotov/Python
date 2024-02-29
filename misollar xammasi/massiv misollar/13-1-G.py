import random
from math import*
N = int(input("N ="))
a = []
P = 1
for i in range(N):
    z = random.randint(1,N)
    a.append(z)
    P = P * fabs(z)
print(a)
print(P)