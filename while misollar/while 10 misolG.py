from math import*
N = int(input("N ="))
i = 1
J = 1
P = 0
s = 0
g = 0
while i <= N:  
    while J <= i:
        G = cos(J)
        S = sin(J)
        g = G + g
        s = S + s
        J = J + 1
    P = (g/s)+P
    g = 0
    s = 0
    J = 1
    i = i + 1
print(P)