import random
#### 1 misol 
# N = int(input("N ="))
# X = int(input("X ="))
# S = 0
# for i in range(1,N+1):
#     P = 1
#     for j in range(1,X*2):
#         P = P *(X * n)
#     S =+ (x**(2+X))//P
# print(S)

##### 2 misol

# N = float(input("N ="))
# S = 0 
# i = 10.2
# while i < N:
#     S = S + i 
#     i += 2
# print(S)



#####  5 Misol
# N = int(input("N ="))
# S = 0
# P = 0
# for i in range(1,N+1):
#     if N % i == 0:
#         S = S + 1
#         # print(S)
#         # print(i)
#         P = P + i / S
# print(P)
    # P = P + i
    # print(P)



        ### 4 Misol
# N = int(input("N ="))
# i = 1.3
# s = 1
# g= 3.3
# while i <= N:
#     s *= i
#     i +=g
#     g += 2
# print(s)

        # 6 Misol
# N = int(input("N = "))
# S = 0
# for i in range(N):
#     a= []
#     for j in range(N):
#         z=random.randint(1,5)
#         a.append(z)
#         S = S + z
#     print(a)
#     print(S)



        ###7 Misol
# N = int(input("N = "))
# S = 0
# for i in range(N):
#     a= []
#     for j in range(N):
#         z=random.randint(1,5)
#         a.append(z)
#         S = S + z
#     print(a)
#     print(S/(N*N))


        ### 9  Misol
# N = int(input("N ="))
# S = 0
# for i in range(1,N+1):
#     S = ((-1)**i)*((x(4**(i+1))/(4*i+1))
# print(S)


            ### 10 Misol
# N = int(input("N ="))
# a = []
# for i in range(N):
#     z=random.randint(1,99)
#     a.append(z)
#     if z % 3 == 0:
#         print(z)
# print(a)

            #### 11 Misol
# a =[81,32,65,23,10,2,543,4,5,6]
# n = len(a)
# for i in range(n-1):
#     for j in range(n-1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1] ,a[j]
# print(a)


            ##### 12 Misol
# a = [23,13,44,65,20,1,4,7,99,0]
# mas_soni = len(a)
# for i in range(mas_soni-1):
#     for j in range(mas_soni-1):
#         if a[j] < a[j+1]:
#             a[j] ,a[j+1] = a[j+1], a[j]
# print(a)

                ### 16 Misol
# N = int(input("N ="))
# S = 0
# for i in range(1,N+1):
#     if N % i == 0:
#         print("bo'linuvchilar soni =", i)
#         S = S + i
# print("Yig'indisi =", S)

                #### 17 Misol
# N = int(input("N = "))
# for i in range(1,N+1):
#     S = 0
#     for j in range(1,N+1):
#         if i % j == 0:
#             S += 1
#     if S == 2:
#         print(i)
#     if N % i == 0 :
#         S = S + 1
# if S == 2:
#     print('tub')
# else:
#     print('tubmas')


            #### 19 Misol
# S = 0
# for i in range(7,2007+10,10):
#     for j in range(11,2011+10,10):
#         S = S + i/j
#         print(S)


            ### 20 Misol
# N = int(input("N ="))
# S = 0
# for i in range(1,N+1):
#     S = (-1)**(i+1)/ (i *(2*i+1)) + S
# print(S)



            ### 21 Misol
# S = 0
# for i in range(20,250+1,1):
#     S = S + i
#     print(S)



            ##23 Misol
# N = int(input("N = "))
# a = []
# for i in range(N):
#     z = random.randint(1,N)
#     if z % 2 != 0:
#         a.append(z)
# print(a)

        ### 24 Misol
# N = int(input("N = "))
# a = []
# for i in range(N):
#     z = random.randint(1,N)
#     if z % 2 == 0:
#         a.append(z)
# print(a)

            ## 25 Misol*
# N = int(input("N = "))
# for i in range(1,N+1):
#     n1 = str(i)
#     n2 = len(n1)
#     n3 = int(n1[n2-1])
#     if n3 != 0:
# # print(n3)
#         if n3 % 3 == 0:
#             print(i)
# print(d[f-1])
# print(c)
# print(p)
# if len(c)-1 % 3 == 0:
#     print("uchga karrali", c)
# else:
#     print("karrali mas", c)


            #####  18 misol
# N = int(input("N ="))
# for i in range(1,N+1):
#     n1 = str(i)
#     n2 = len(n1)
#     d = 0 
#     for j in range(1,int(n2+1)):
#         g = int(str(i)[-j])
#         d += g**3
#     if d == i:
#         print(i)


    #     n3 = int(n1[j])
    # # print(n3)
    #     n4 = int(n1[n2-j])
    #     n5 = int(n1[n2-j])
    # # print(n3,n4,n5)
    #     d = n3**3+n4**3+n5**3
    #     if d == i:
    #         print(i)

# for kub in range(1,N+1):
#     for i in range(1,kub+1):
#         # i**3
#         for j in range(1,i+1):
#             # j**3 
#             for k in range(1,j+1):
#                 # k**3 
#                 d = i**3+j**3+k**3
#                 if kub == d:
#                     print(kub,"=",i,"+",j,"+",k)




# S = 0
# N = int(input("N ="))
# for i in range(1,N+1):
#     for j in range(1,i+1):
#         for k in range(1,j+1):
#             for l in range(1,k+1):
#                 for m in range(1,l+1):
#                     for o in range(1,m+1):
#                         S = S + o
# print(S)



N = int(input("N ="))
a = []
for i in range(1,N+1):
    for j in range(1,i+1):
        z =  random.randint(1,100)
        if z % 2 != 0 :
            a.append(z)
            s =len(a)
            if N == s:
                print(a)
                break