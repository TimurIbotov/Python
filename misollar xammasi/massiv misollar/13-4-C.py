import random
N = int(input("N ="))
a = []
S = 0
for i in range(N):
    z = random.randint(1,N)
    a.append(z)
    S = S + z / N
print(a)
print(S)