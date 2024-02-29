from math import*
import random 
N = int(input("N ="))
z = 0 
P = 1
m = []
for i  in range(0,N):
    z = random.randint(1,N)
    P = P * fabs(z)
    m.append(z)
print("m =", m)
print("P =", P)