N =int(input("N ="))
X = int(input("X ="))
S = 0
P = 1
for i in range(N+1):
    P = P * i
    S = ( X**i / P ) + S 
print(S) 