A = float(input("A ="))
N = int(input("N ="))
S = 0
P = 1
for i in range(1 , N + 1):
    for J in range(1 , i + 1):
        M = (A - 1 +J )
        P = P * M
    S = S + (1/P)
    P = 1
print("S = ",S )