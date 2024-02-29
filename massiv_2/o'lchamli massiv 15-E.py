N = int(input("N ="))
a = []
for i in range(0,N):
    for j in range(0,N):
        if i == j:
            a.append(2)
        elif i == j + 1 or i == j - 1:
            a.append(1)
        else:
            a.append(0)
    print(a)
    a=[]