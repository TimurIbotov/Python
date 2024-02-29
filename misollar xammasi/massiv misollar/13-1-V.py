import random
from math import*
N = int(input("N ="))
a = []
S = 0
for i in range(N):
    z = random.randint(1,N)
    a.append(z)
    S = S + fabs(z)
print(a)
print(S)