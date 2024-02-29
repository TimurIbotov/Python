from math import*
N = int(input("N ="))
X = float(input("X ="))
S = 1
P = 1
for i in range(1, N+1 ):
    S = S * i
    P = (1+ ((sin(i*X))/ S)) * P
print(P)