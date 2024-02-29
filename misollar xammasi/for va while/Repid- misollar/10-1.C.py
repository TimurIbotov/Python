N = int(input("N ="))
S = 0
for i in range(N+1):
    S =  1/ ((2 * i + 1)**2) + S
print(S)