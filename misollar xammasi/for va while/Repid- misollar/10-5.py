from math import*
Q = int(input("Q ="))
R = int(input("R ="))
B = int(input("B ="))
C = int(input("C ="))
D = int(input("D ="))
N = int(input("N ="))
X = 0
x0 = C
x1 = D
for i in range(2,N+1):
    X = Q * x1 + R * x0 + B
    x0 = x1
    x1 = X
print(X)