N = int(input("N ="))
A = int(input("A ="))
S = 1/A
for i in range(1,N+1):
    s = A
    for j in range(1,i+1):
        s = (A * i) * S
    S = S + 1/s
print(S)