import random
N = int(input("N ="))
a = []
for i in range(N):
    z = random.randint(-5,N)
    a.append(z)
print(a)
P = 1
for j in a:
    if j > 0:
        P = P * j
    elif j <= -1:
        break
print(P)