import random
N = int(input("N ="))
a = []
S = 0
for i in range(1,N+1):
    z = random.randint(1,N)
    a.append(z)
    S = S + z
print(a)
print(S)