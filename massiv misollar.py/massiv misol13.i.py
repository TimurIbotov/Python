import random
N = int(input("N ="))
z = 0
S = z/1
P = 1
m = []
for i in range(1,N+1):
    P = P * (i)
    print(P)
    z = random.randint(1,N)
    S = (z/P) + S
    m.append(z)
print("M =", m)
print("S =", S)