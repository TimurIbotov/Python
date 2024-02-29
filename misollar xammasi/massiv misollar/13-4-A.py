import random
N = int(input("N ="))
z = 0 
a = []
S = 0
for i in range(1, N+1):
    z = random.randint(-5,N)
    a.append(z)
print(a)
for j in a:
    if j > 0:
        S = S + j
    elif j <= -1:
        break
print(S)