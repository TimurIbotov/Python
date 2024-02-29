N = int(input('N ='))
i = 1
S = 0
J = 1
P = 1

while i <= N:
    J = i
    while J < i*2:
        P = P * (J + 1)
        J += 1
    S = S + P 
    i += 1
print("S =", S)