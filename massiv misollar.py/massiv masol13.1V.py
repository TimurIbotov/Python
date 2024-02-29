from math import*
import random
N = int(input("N ="))
m = []
z = 0 
S = 0
for i in range(0,N):
    z =random.randint(0, N)
    S = S + fabs(z)
    m.append(z)
print("m =", m)
print("S =", S)