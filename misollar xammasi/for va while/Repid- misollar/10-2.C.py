from math import*
N = int(input("N ="))
X = int(input("X ="))
S = 0 
for i in range(1,N+1):
    S = (X + cos(i*X)) / 2 ** i + S
print(S)