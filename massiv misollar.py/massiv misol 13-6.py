# # N = int(input("N ="))
# # m = []
# # z = 0
# # for i in range(1,N+1):
# #     z=random.randint(1,N)
# #     m.append(z)
# #     for j in range(1,i+1):
# for k in range(N+1):
#     z = random.randint(1,N)
#     m.append(z)
# print(m)
def MyMassSort(m):
    import random
    f = []
    for k in range(m):
        c = random.randint(1,m)
        f.append(c)
    print(f)
    n = len(f)
    qadam = 0
    for i in range(n-1):
        for j in range(n-1):
            if f[j] > f[j+1]:
                qadam += 1
                f[j], f[j+1] = f[j+1], f[j]
    return(f)
    print(qadam)
N = int(input("N = "))
a = MyMassSort(N)
print(a)

# N = int(input("N ="))
# m = []
# z = 0 
# qadam = 0
# a = 0
# for i in range(1,N+1):
#     z = random.randint(1,N)
#     m.append(z)
#     n = len(m)
# for j in range(n-1):
#     if m[z] > m[j]:
#         m[j] = m[i]
# print("M =", m)
# print("qadam =", qadam)
# N = int(input("N ="))
# z = 0
# m = []
# a = []
# min = 0
# for i in range(0,N):
#     z = random.randint(1,N)
#     m.append(z)
#     for j in range(i,i+1):
#         if min < z:
#             min = z
#         a.append(min)
#     min = 0
# print("M =", m)
# print("A =", a)


# a=[23,-6,"sdr",True,3,4,6,8,-1,2323,999]
# for j in range(1,len(a),2):
#     print(a[j])
# print(m)