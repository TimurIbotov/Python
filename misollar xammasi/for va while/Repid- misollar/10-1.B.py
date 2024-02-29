N = int(input("N ="))
S = 0
for i in range(N+1):
    S = 1/i**5 + S
print(S)