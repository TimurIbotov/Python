from math import*
N = int(input("N ="))
S = 0
for i in range(1,N+1):
    for j in range(1,i+1):
        S = 1/(sin(j))+S
print(S)