from math  import*



N = int(input("N ="))
s = sin(1)
S = 1/(sin(1))
for i in range(2, N+1):
    s = s + sin(i)
    S = S + 1/ s
print("S =", S)