from math import*
N = int(input("N ="))
X = int(input("X ="))
S = 1
P = 1
for i in range(N+1):
    S = S * i
    P = (1+(sin(i*X)/S)) * P
print(P)