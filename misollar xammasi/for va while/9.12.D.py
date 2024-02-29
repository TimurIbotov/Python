A = int(input("A ="))
N = int(input("N ="))
S = 1
for i in range(N):
    s = (A - i * N)
    S = S * s
print(S)