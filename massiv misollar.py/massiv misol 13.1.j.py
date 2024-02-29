import random
N = int(input("N ="))
z = 0 
S = 0
m = []
for i in range(1,N):
    z = random.randint(0,N)
    S = (((-1)**(i))*z) + S
    m.append(z)
print("M =", m)
print("S =", S)