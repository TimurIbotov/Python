N = int(input("N ="))
for i in range(1,N+1):
    if i % 3 == 0 and i % 5 != 0:
        print(i)