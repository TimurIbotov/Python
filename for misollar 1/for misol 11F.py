N = int(input("N ="))
P = 1
S = 1
for j in range(2, N+1):
    for i in range(2, j+1):
        S = S * i
    P = ((1+ (1/S))**2) * P
    S = 1
print("P = ", P)