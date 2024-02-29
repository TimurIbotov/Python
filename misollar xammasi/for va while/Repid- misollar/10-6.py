N =int(input("N ="))
A = 0
a0 = 1
a1 = 1
for i in range(2,N+1):
    A = a0 + (a1/(2**i-2))
    a0 = a1
    a1 = A
print(A)