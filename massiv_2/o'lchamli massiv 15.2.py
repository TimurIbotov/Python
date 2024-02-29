import random 
N = int(input("N ="))
M = int(input("M ="))
m = []
a = []
z = 0
S = 0
max = 0
for i in range(1,M+1):
    for j in range(1,N+1):
        z = random.randint(1,N)
        a.append(z)
        S = S + z
        if max < S:
            max = S
    a.append(S)
    S = 0
    print(a)
    m.append(a)
    a = []

print(m)