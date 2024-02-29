N = int(input("N ="))
for i in range(1,N+1):
    S = 0
    for j in range(1,i+1):
        if i % j == 0:
            S = S + 1
    if S == 2:
        print(i)