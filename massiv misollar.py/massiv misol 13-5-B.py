import random
N = int(input("N ="))
z = 0 
m = []
min = N
for i in range(1,N+1):
    z = random.randint(0,N)
    m.append(z)
    if min > z:
        min = z
print("min =", min)
print("M =", m)