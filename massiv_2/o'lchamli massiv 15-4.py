import random 
N = int(input("N ="))
M = int(input("M ="))
a = []
z = 0
S = 0
max = 0
m =[]
g =[]
for i in range(1,M+1):
    for j in range(1,N+1):
        z = random.randint(1,N)
        a.append(z)
    print(a)
    m.append(a)
    a = []
for k in range(M):
    for l in range(N):
        if max < m[l][k]:
            max = m[l][k]
    g.append(max)
    max = 0
print(g)
# print(m)
# for k in range(0,N-1):
#     for M in range(0,M-1):
#         if max < g[i-1][j-1]:
#            max = g[i-1][j-1]
#     m.append(max)
#     max = 0
    
# print(m)