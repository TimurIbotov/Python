from math import*
import random 
# x = int(input("X ="))
# y = int(input("y ="))
# z = int(input('z ='))
# S = x + y + z
# P = x * y * z
# if S > P:
#     print("S katta")
# else:
#     print("P katta")

# x = int(input("X ="))
# y = int(input("y ="))
# z = int(input('z ='))
# S = x + y + (z/2)
# P = x * y * z
# x1 = min(S,P)
# x1 = (x1**2 +1)

# a = int(input("a ="))
# b = int(input("b ="))
# c = int(input("c ="))
# D = (b**2) - 4 * a * c
# if a == 0:
#     print("yechimga ega emas")
# elif D == 0:
#     X1 = -b / a * 2
#     print(X1)
# elif D < 0:
#     print("chiziqli teglama")
# else:
#     X1 = -b -sqrt(D)/ 2 * a
#     X2 = -b + sqrt(D)/ 2 * a
# print(X1, X2)
# N = int(input("N ="))
# S = 0
# for i in range(1,N+1):
#     S = 0
#     for j in range(1,i+1):
#         if i % j == 0:
#             S = S + 1
#     if S == 2:
#         print(i)
# N = int(input("N ="))
# for i in range(N + 1):
#     for j in range(2 * i):
#         S = S + (j * (i+1))
# print(S)
# N = int(input("N ="))
# a0 = 1
# for i in range(1,N+1):
#     A = i * a0 + 1/i
#     a0=A
# print("A =", A)
N = int(input("N ="))
m = []
for i in range(1,N+1):
    z = random.randint(1,N+1)
    m.append(z)
print(m)