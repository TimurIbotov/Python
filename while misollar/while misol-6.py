from math import*
N = int(input("N ="))
i = 2
P = 1
while i <= N:
    P = (i + 1) / (i + 2) * P
    i += 1
print("P =", P)