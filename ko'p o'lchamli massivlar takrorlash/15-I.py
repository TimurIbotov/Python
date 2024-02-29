N = int(input("N ="))
a = []
for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j:
            a.append(i)
        elif i == N+1-j:
            a.append(j)
        else:
            a.append(0)
    print(a)
    a=[]