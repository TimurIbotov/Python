from math  import*
N = int(input("N ="))
S1 = cos(1) / sin(1)
S = 0
for i in range(2, N+1):
    S1 = S1 + cos(i) / sin(i)
    S = S + S1
print("S =", S)