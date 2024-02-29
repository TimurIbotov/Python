N = int(input("N ="))
S = 0
for c in range(1,N+1):
    S =  c ** 2
    for a in range(1,c+1):
        for b in range(1,a+1):
            D = a ** 2 + b ** 2
            if S == D:
                print("Pifagor sonlar", b, a ,c)
    S = 0