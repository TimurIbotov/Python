import random
N = int(input("N ="))
z = 0
S = 0 
P = 1
m = []
for i in range(0,N):
    z = random.randint(1,N)
    for J in range(1,i):
        P = P * J
        S = (((-1)**i)*z / P) + S
    m.append(z)
print("M =", m)
print("S =", S)