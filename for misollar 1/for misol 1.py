N = int(input("N ="))
S = 0
K = 0
for i in range (1 , N + 1, 1):
    if N % i == 0 :
        print("i = ", i)
