N = int(input("N ="))
S = 0
for i in range(1,N):
    if N % i == 0:
        print(i)
        S = S + i
if S == N:
    print("mukkamal son")
else:
    print("mukammal son emas")