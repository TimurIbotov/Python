from math import*
N = int(input("N ="))
a = 1
b = 1 
c = 1
while c <=N:
    C = pow(c,2)
    while a <= c:
        while b <= a:
            D = pow(a,2) + pow(b,2)
            if C == D:
                print("Pifagor sonlar", a, b, c)
            b += 1
        b=1
        a += 1
    a = 1
    c += 1
    C = 0
    
    # while b <= a:
    #     while c <= b:
    #         S  = pow(a,2)+ pow(b,2)
    #         C=pow(c,2)
    #         # print(S)
    #         if C == S:
    #             print("Pifagor sonlar")
    #         c += 1
    #     C=0
    #     b = b + 1
    # a = a + 1
    # b = 1
    # c=1
    # S=0