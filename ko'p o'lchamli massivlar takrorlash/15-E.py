N = int(input("N ="))
for i in range(1,N+1):
    a = []
    for j in range(1,N+1):
        if i == j :
            a.append(2)
        elif i == j+1 or i == j-1:
            a.append(1)
        else:
            a.append(0)
    print(a)