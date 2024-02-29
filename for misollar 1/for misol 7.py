N = int(input("N ="))
S = 0
for i in range(1, N):
    for j in range (1 , i+ 1):
        if i % j == 0:
            S = S + 1
    if S == 2:
        print(j)
    S = 0