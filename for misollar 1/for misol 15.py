N = int(input(" N = "))
S = 0
P = 1
for i in range(1, N+1 ):
    for J in range(i, i*2):
        P = P * (J + 1)
        # print(J)
    S = S + P
print("S =", S)