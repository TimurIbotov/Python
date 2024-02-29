N = int(input("N ="))
P = 1
S = 0
for i in range(1,N+1):
    for j in range(i,i*2):
        P = P * (j + 1)
    S = S + P
print(S)