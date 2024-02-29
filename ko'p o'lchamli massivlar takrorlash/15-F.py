N = int(input("N ="))
for i in range(1,N+1):
    a = []
    for j in range(0,N):
        if (N+1)-i > j :
            a.append(i)
        else:
            a.append(0)
    print(a)