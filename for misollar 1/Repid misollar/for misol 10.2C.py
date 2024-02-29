from math import*
N = int(input("N ="))
X = float(input("X ="))
S = 0
for i in range(1 , N + 1):
    S = (X + (cos(i*X))) / pow(2,i) +S
print("S =", S)