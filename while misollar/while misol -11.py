from math import*
N = int(input("N ="))
i = 0
a = 1
S = 1
while i <= N:
    S = (a + (sin(N)))* S
    i += 0.1    
print("S =",S)
