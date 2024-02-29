N = int(input("N ="))
S = 0
for i in range(1,N+1):
    a = []
    for j in range(1,i+1):
            S = S  + 1 
            a.append(S)
    print(a)