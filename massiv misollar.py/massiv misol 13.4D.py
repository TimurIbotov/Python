import random
N = int(input("N ="))
z = 0
m = []
P = 1
for i in range(1,N+1):
    z = random.randint(1,N)
    m.append(z)
    P = (P * z)**(1/N) 
print("P =", P)
print(m)