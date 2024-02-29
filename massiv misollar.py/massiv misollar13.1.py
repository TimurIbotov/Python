
import random
N = int(input("N ="))
m = []
i = 0
z = 0
S = 0
while i <= N:
    z = random.randint(0, N)
    i += 1
    S = S + z
    m.append(int(z))
print("m = ", m)
print(S)