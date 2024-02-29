from math import *
import random
class shart:
    def misol9_1(N):
        for i in range(1,N+1):
            if N % i ==0:
                print(i)
    def misol9_2(N):
        S = 0
        for i in range(1,N+1):
            if N % i == 0:
                print(i)
                S = S + i
        print(S)
    def misol9_3(N):
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
    def misol9_4(N):
        S = 0 
        for i in range(1,N+1):
            for j in range(1,i):
                if i % j == 0 :
                    S = S + j
            if S == i:
                print(S)
            S = 0
    def misol9_5(N):
        for i in range(1,N+1):
            if i % 3 == 0 and i % 5 != 0:
                print(i)
    def misol9_6(N):
        S = 0
        for i in range(1,N+1):
            if N % i == 0:
                S = S + 1
        if S == 2:
            print("tub son")
        else:
            print("Tub emas")
    def misol9_7(N):
        for i in range(1,N+1):
            S = 0
            for j in range(1,i+1):
                if i % j == 0:
                    S = S + 1
            if S == 2:
                print(i)
    def misol9_8(N):
        S = 0
        for c in range(1,N+1):
            S =  c ** 2
            for a in range(1,c+1):
                for b in range(1,a+1):
                    D = a ** 2 + b ** 2
                    if S == D:
                        print("Pifagor sonlar", b, a ,c)
            S = 0
    def misol9_10A(N):
        P = 1
        for i in range(N+1):
            P = (1 + (1/i**2)) * P
        print(P)
    def misol9_10B(N):
        P = 1
        for i in range(1,N+1):
            P = P * i
        print(P)
    def misol9_10D(N):
        S = sqrt(2)
        for i in range(N+1):
            S = sqrt+(S+2)
        print(S)
    def misol9_10E(N):
        S = sqrt(2)
        for i in range(N+1):
            S = sqrt+(S+2)
        print(S)
    def misol9_10F(N):
        S = 0
        for i in range(1,N+1):
            for j in range(1,i+1):
                S = 1/(sin(j))+S
        print(S)
    def misol9_10G(N):
        S = 0
        a = 0
        b = 0
        for i in range(1,N+1):
            for j in range(1,i+1):
                a = cos(j) + a
                b = sin(j) + b
            S = a / b + S
        print(S)
    def misol9_11A(N):
        S = 0
        for i in range(N + 1):
            S = 1 / i**2 + S
        print(S)
    def misol9_11B(N):
        S = 0
        for i in range(N+1):
            S = S+ (1/ i**3)
        print(S)
    def misol9_11C(N):
        S =  0
        P = 1
        for i in range(N+1):
            P = P * i
            S = S + (1/P)
        print(S)
    def misol9_11D(N):
        S = 0 
        for i in range(N+1):
            S =  1/ ((2*i)**2)
        print("S =", S)
    def misol9_11E(N):
        P = 1
        for i in range(N+1):
            P = P * (i+1/i+2)
        print(P)
    def misol9_11F(N):
        S = 1
        P = 1
        for i in range(1,N+1):
            S = S * i
            P = P *(1+1/S)
        print(P)
    def misol9_12A(N,A):
        P = 1
        for i in range(N+1):
            s = A + i - 1
            P *=s
        print(P)
    def misol9_12C(N,A):
        S = 1/A
        for i in range(1,N+1):
            s = A
            for j in range(1,i+1):
                s = (A * i) * S
            S = S + 1/s
        print(S)
    def misol9_12D(A,N):
        S = 1
        for i in range(N):
            s = (A - i * N)
            S = S * s
        print(S)
    def misol13(N):
        i = 0,1
        P = 1
        while i <=N:
            P = (1 + sqrt(i)) * P
            i = i + 0,1
        print(P)
    def misol14(N,A,X):
        P = 1
        P = (X + A) ** 2
        for i in range(2, N +1):
            P = ((P + A)** 2)
        print("P =", P)
    def misol15(N):
        P = 1
        S = 0
        for i in range(1,N+1):
            for j in range(i,i*2):
                P = P * (j + 1)
            S = S + P
        print(S)
# shart.misol9_1(7)
# shart.misol9_2(7)
# shart.misol9_3(7)
# shart.misol9_4(7)
# shart.misol9_5(7)
# shart.misol9_6(7)
# shart.misol9_7(7)
# shart.misol9_8(7)
# shart.misol9_10A(5)
# shart.misol9_10B(5)
# shart.misol9_10D(5)
# shart.misol9_10E(8)
# shart.misol9_10F(5)
# shart.misol9_10G(4)
# shart.misol9_11A(5)
# shart.misol9_11B(4)
# shart.misol9_11C(3)
# shart.misol9_11D(6)
# shart.misol9_11E(5)
# shart.misol9_11F(8)
# shart.misol9_12A(5,6)
# shart.misol9_12C(5,7)
# shart.misol9_12D(5,5)
# shart.misol13(3)
# shart.misol14(5,5,5)
# shart.misol15(10)
print(QQ)
