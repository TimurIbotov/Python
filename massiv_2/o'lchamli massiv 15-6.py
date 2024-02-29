# import random 
# # N = int(input("N ="))
# # M = int(input("M ="))
# # m = []
# # a = []
# # z = 0
# # S = 0
# # min = N
# # x=0
# # for i in range(1,M+1):
# #     for j in range(1,N+1):
# #         z = random.randint(1,N)
# #         a.append(z)
# #         if min > z:
# #             min = z
# #             x=j
# #     print(a)
# #     a.pop(x-1)    
# #     m.append(a)
# #     print(a)
# #     a = []
# #     print(min)
# #     min=N
# N = int(input("N ="))
# M = int(input("M ="))
# a = []
# z = 0
# m = []
# S = 0
# min = N
# g =[]
# for i in range(1,M+1):
#     for j in range(1,N+1):
#         z = random.randint(1,N)
#         a.append(z)
#     print(a)
#     m.append(a)
#     a = []
# for k in range(M):
#     for l in range(N):
#         if min > m[l][k]:
#             min = m[l][k]
#     g.append(min)
#     g.pop(x-1)
#     min = N
# m.append(g)
# print(g)
# print(m)