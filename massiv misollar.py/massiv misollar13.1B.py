import random
N = int(input("N ="))
m = []
z = 0
P = 1
for i in range(0,N):
    z = random.randint(0, N)
    P = P * z
    m.append(int(z))
print("m =", m)
print(P)
