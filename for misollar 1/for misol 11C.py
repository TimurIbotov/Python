N = int(input("N ="))
S = 0
P = 1
for j in range(1, N +1):
    for i in range(1 , j+1):
        P = P * i
    S = (1/P) + S
    P = 1
print("S =", S)