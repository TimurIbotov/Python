N =int(input("N ="))
S = 1
P = 1
for i in range(1,N+1):
    S = S * i
    P = P *(1+1/S)
print(P)