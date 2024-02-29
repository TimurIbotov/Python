from math import*
N = int(input("N ="))
S = 1
for i in range(1, N+1):
    S = (1 + 1/ pow(i,2))
print(S)