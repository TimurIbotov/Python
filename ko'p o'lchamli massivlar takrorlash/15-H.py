N = int(input("N ="))
for i in range(1,N+1):
    a = []
    for j in range(1,N+1):
        if i <= j:
            a.append(N+i-j)
        else:
            a.append(0)
    print(a)
("Hello world")