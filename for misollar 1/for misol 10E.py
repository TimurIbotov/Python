from math import*
N = int(input("N ="))
S = 0
P = 0
for i in range(0, N):
    S = (3 * (N -i))
    P = sqrt(S+P)
print(P)