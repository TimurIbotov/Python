from math import*
N = int(input('N ='))
i = 1
P = 1
S = 0
J = 1
while J <= N:
    while i <= J:
        P = P * i
        i += 1
    J += 1
    i = 1
    S =(1/P)+S
    P = 1
print("S =", S)