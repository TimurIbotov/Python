N = int(input("N ="))
P = 1
for i in range(N+1):
    P = P * (i+1/i+2)
print(P)