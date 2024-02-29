import random 
N = int(input("N ="))
M = int(input("M ="))
m = []
a = []
max = 0
for i in range(1,M+1):
    for j in range(1,N+1):
        z = random.randint(1,N)
        a.append(z)
        if max < z:
            max = z
    a.append(max)
    max = 0
    print(a)
    m.append(a)
    a = []
print(max)