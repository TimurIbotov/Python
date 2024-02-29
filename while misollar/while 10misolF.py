from math import*
N = int(input("N ="))
i = 1
J = 1
P = 0
s = 0
while i <= N:  
    while J <= i:
        S = sin(N)
        s = S + s
        J = J + 1
    P = 1/s
    s = 0
    J = 1
    i = i + 1
print(P)