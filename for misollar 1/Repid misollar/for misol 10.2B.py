from math import*
N = int(input("N ="))
X = float(input("X ="))
S = 0
P = 1
for i in range(1, N+1):
    P = P * i
    S = ((1/P) + (sqrt(fabs(X)))) + S
print("S =", S)