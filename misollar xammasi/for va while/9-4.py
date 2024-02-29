N = int(input("N ="))
S = 0 
for i in range(1,N+1):
    for j in range(1,i):
        if i % j == 0 :
            S = S + j
    if S == i:
        print(S)
    S = 0