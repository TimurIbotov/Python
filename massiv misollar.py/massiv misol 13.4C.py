import random
N = int(input("N ="))
z = 0
m = []
S = 0
for i in range(1,N+1):
    z = random.randint(0,N)
    m.append(z)
    S = S + z
    P = S / N
print(S)
print(P)
print(m)