from math import*

A = float(input("A = "))
N = int(input("N = "))
i = 1 
S = 0
z = 1
c=1
while i <= N:
    while z <= i:
        M = (A - 1 + z)
        c=c*M
        
        z += 1
    S=S+(1/c)
    i += 1
    z = 1
    c=1
print("S =", S)