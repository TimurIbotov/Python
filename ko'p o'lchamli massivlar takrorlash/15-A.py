N = int(input("N ="))
a = []
for i in range(N):
    for j in range(N):
        if i == j:
            a.append(1)
        else:
            a.append(0)
    print(a)
    a = []