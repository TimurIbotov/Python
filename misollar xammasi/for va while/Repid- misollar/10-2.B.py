from math import*
N = int(input("N ="))
X = int(input("X ="))
P = 1
S = 0
for i in range(N+1):
    P = P * i
    S = (1/P +sqrt(fabs(X))) + S
print(S)