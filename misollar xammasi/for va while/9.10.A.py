N = int(input("N ="))
P = 1
for i in range(N+1):
    P = (1 + (1/i**2)) * P
print(P)
