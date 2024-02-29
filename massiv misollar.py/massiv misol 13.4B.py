#     print(b)
import random
N = int(input("N ="))
z = 0 
a = []
S = 1
for i in range(1, N):
    z = random.randint(-5,N)
    a.append(z)
    if z < 0:
        print(z)
        S = S * z
print("S =", S)
print(a)