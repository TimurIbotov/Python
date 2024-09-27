N = int(input("N ="))
for i in range(1,N+1):
    a = []
    for j in range(1,N+1):
        if i <= j:
            a.append(N+i-j)
        else:
            a.append(0)
    print(a)
("Hello world")
# N = int(input("N = "))
# S = 0
# for i in range(1,N+1):
#     if N % i == 0:
#         S = S + 1
# if S == 2:
#     print("Tubson")
# else:
#     print("tub emas")
# N = float(input("N = "))
# B = float(input("B = "))
# if N > B :
#     print(N)
# else:
#     print("N = ",N,'B =',B)
# N = int(input("N ="))
# for i in range(N):
#     if i % 3 ==0 and i % 5 !=0:
#         print(i)
# A = float(input("A ="))
# B = float(input("B ="))
# if 1 <= A and A <= 9:
#     print("1,va 9 oraliqida bor")
# else:
#     print("Yoq")
# if 1 <= B and B <= 9:
#     print("1,va 9 oraliqida bor")
# else:
#     print("Yoq")