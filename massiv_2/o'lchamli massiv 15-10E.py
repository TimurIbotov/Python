N = int(input("N ="))
a = []
for i in range(N):
    for j in range(N, 0, -1):
        if i <= j-1:
            a.append(1)
        else:
            a.append(0)
    print(a)
    a = []