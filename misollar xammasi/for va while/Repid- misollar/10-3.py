N = int(input("N ="))
A = 0
a0 = 1
for i in range(1,N+1):
    A = i * a0 + 1/i
    a0 = A
print(A)