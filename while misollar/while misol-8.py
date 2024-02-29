from math import*
A = float(input(" A = "))
N = int(input(" N = "))
i = 1
S = 1
while i <= N:
    z =  (A + i - 1)
    i += 1
    S = S * z
print(S)