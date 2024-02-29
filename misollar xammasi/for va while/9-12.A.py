N =int(input("N ="))
A = int(input("A ="))
P = 1
for i in range(N+1):
    s = A + i - 1
    P *=s
print(P)