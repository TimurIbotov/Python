N = 5
a = []
for i in range(1,N+1):
    for j in range(0,N):
        if (N + 1) - i > j:
            a.append(i)
        else:
            a.append(0)
    print(a)
    a = []