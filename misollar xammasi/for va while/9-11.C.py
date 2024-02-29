N =int(input("N ="))
S =  0
P = 1
for i in range(N+1):
    P = P * i
    S = S + (1/P)
print(S)