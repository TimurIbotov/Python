import random 
N = int(input("N ="))
M = int(input("M ="))
m = []
a = []
z = 0
S = 0
min = N
for i in range(1,M+1):
    for j in range(1,N+1):
        z = random.randint(1,N)
        a.append(z)
        if min > z:
            min = z
    print(a)
    m.append(a)
    a = []
    print(min)
    min = N