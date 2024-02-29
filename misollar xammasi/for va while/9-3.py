N= int(input("N ="))
S = 0
for i in range(1,N):
    if N % i ==0:
        print(i)
        S = S + i
        print(S)
if N == S:
    print("mukammal son")
else:
    print("mukammal emas")