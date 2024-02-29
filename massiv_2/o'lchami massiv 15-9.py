import random
# # M = int(input("M ="))
# # N = int(input("N ="))
# # A = []
# # X = []
# # for i in range(M):
# #     for j in range(N):
# #         z = random.randint(1,9)
# #         A.append(z)
# #     print(A)
# #     A= []
# #     X.append(A)
# # for k in range(M):
# #     min = N
# #     for l in range(N):
# #         if min > X[l][k]:
# #             min = X[l][k]
# #     print(min)
# N = int(input("N ="))
# M = int(input("M ="))
# a = []
# m = []
# g =[]
# for i in range(1,M+1):
#     for j in range(1,N+1):
#         z = random.randint(1,9)
#         a.append(z)
#     print(a)
#     m.append(a)
#     a = []
# print(m)
# for k in range(M):
#     q = N
#     for l in range(N):
#         if q > m[l][k]:
#             q = m[l][k]
#             s = 0
#             b = 0
#             s = m[l][k]
#             b = m[0][k]
#             m[0][k] = s
#             m[l][k] = b
#     print(q)
# print(m)
M = int(input("M ="))
N = int(input("N ="))
a = []
X = []
for i in range(M):
    for j in range(N):
        z = random.randint(1,15)
        a.append(z)
    X.append(a)
    print(a)
    a = []
print(X)
eng_katta = 0
eng_katta_index = 0
sana = 0
for k in range(len(X)):
    for l in range(len(X)):
        if eng_katta < X[l][k]:
            eng_katta = X[l][k]
            eng_katta_index = sana
    sana += 1
xnol = 0
for m in range(0,len(X)):
    for b in range(0,len(X[m])):
        xnol = X[b][0]
        X[b][0] = X[b][eng_katta_index]
        X[b][eng_katta_index] = xnol
print(X)
# for i in X:
#     print(i)

# for k in range(len(X)):
#     for l in range(k+1):
#         if eng_katta <= X[l][k]:
#             eng_katta = X[l][k]
#             eng_katta_index = sana
#         print(eng_katta,sana)
#     sana += 1


