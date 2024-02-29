from math import*
N =int(input("N ="))
S = 0
a = 0
b = 0
for i in range(1,N+1):
    for j in range(1,i+1):
        a = cos(j) + a
        b = sin(j) + b
    S = a / b + S
print(S)