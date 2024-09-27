import random 
N = int(input("N ="))
M = int(input("M ="))
z = 0
# S = 0
for i in range(M):
    A = []
    S = 0
    for j in range(N):
        z = random.randint(1,9)
        A.append(z)
        S = S + A[j]
    A.append(S)
    print(A)
