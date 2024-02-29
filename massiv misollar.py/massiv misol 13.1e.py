import random
N = int(input("N ="))
i = 0 
z = 0 
S = 0
P = 1
m = []
while i <= N:
    z = random.randint(1,N)
    S = S + z
    P = P * z
    m.append(z)
    i += 1
print("m =", m)
print("S =", S, "P =", P)