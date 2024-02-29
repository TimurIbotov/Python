import random
# N = int(input("N ="))
# M = int(input("M ="))
# L = int(input("L ="))
# katta_mxn = []
# for i in range(N):
#     nxm = []
#     for j in range(M):
#         z = random.randint(1,4)
#         nxm.append(z)
#     print(nxm)
#     katta_mxn.append(nxm)
# katta_mxl = []
# for k in range(M):
#     mxl = []
#     for l in range(L):
#         a = random.randint(1,4)
#         mxl.append(a)
#     katta_mxl.append(mxl)
#     print("\t",mxl)
# for x in range(0,len(katta_mxl)):
#     mat_Summ = []
#     for m in range(len(katta_mxl)):
#         S = 0
#         P = 1
#         for b in range(len(katta_mxn)):
#             # print(katta_mxn[m][x],katta_mxl[x][b])
#             P = katta_mxn[m][x] * katta_mxl[x][b] 
#             S = S + P
#             # print(S)
#         mat_Summ.append(S)
#         # # print(P)
#         # # print(S)
#     print(mat_Summ)
# print(katta_mxn,"\t",katta_mxl)




# import random
# N = int(input("N ="))
# M = int(input("M ="))
# L = int(input("L ="))
# katta_mxn = []
# for i in range(N):
#     nxm = []
#     for j in range(M):
#         z = random.randint(1,4)
#         nxm.append(z)
#     print(nxm)
#     katta_mxn.append(nxm)
# katta_mxl = []
# for k in range(M):
#     mxl = []
#     for l in range(L):
#         a = random.randint(1,4)
#         mxl.append(a)
#     katta_mxl.append(mxl)
#     print("\t",mxl)
# for x in range(0,len(katta_mxl)):
#     mat_Summ = []
#     for m in range(len(katta_mxl)):
#         S = 0
#         P = 1
#         for b in range(len(katta_mxn)):
#             print(katta_mxn[x][b],katta_mxl[b][m])
#             # P = katta_mxn[m][b] * katta_mxl[b][m] 
#             S = S + P
#             mat_Summ.append(S)
#         print(mat_Summ)
#         mat_Summ = []
#     print(mat_Summ)
# print(katta_mxn,"\t",katta_mxl)


# N = int(input("N ="))
# M = int(input("M ="))
# L = int(input("L ="))
# katta_mxn = []
# for i in range(N):
#     nxm = []
#     for j in range(M):
#         z = random.randint(1,4)
#         nxm.append(z)
#     print(nxm)
#     katta_mxn.append(nxm)
# katta_mxl = []
# for k in range(M):
#     mxl = []
#     for l in range(L):
#         a = random.randint(1,4)
#         mxl.append(a)
#     katta_mxl.append(mxl)
#     print("\t",mxl)
# for x in range(0,len(katta_mxl)):
#     mat_Summ = []
#     for m in range(len(katta_mxl)):
#         S = 0
#         P = 1
#         for b in range(len(katta_mxn)):
#             # print(katta_mxn[m][x],katta_mxl[x][b])
#             P = katta_mxn[x][b] * katta_mxl[m][x] 
#             S = S + P
#             # print(S)
#         mat_Summ.append(S)
#         # # print(P)
#         # # print(S)
#     print(mat_Summ)
# print(katta_mxn,"\t",katta_mxl)



# x = int(input("X = "))
# y = int(input("Y = "))
# if x % 2 == 0:
#     if y % 2 == 0:
#         print("oq")
# if x % 2 != 0:
#     if y % 2 != 0:
#         print("oq")
# if x % 2 == 0:
#     if y % 2 != 0:
#         print("qora")
# if x % 2 != 0:
#     if y % 2 == 0:
#         print("qora")
# N = int(input("N ="))
# M = int(input("M ="))
# L = int(input("L ="))
# MxN_mass= []
# mnx_kich = []
# for i in range(N):
#     for j in range(M):
#         z =  random.randint(1,4)
#         mnx_kich.append(z)
#     MxN_mass.append(mnx_kich)
#     print(mnx_kich)
#     mnx_kich = []
# MxL_mass = []
# mxl_kich = []
# for k in range(M):
#     for m in range(L):
#         random_son = random.randint(1,4)
#         mxl_kich.append(random_son)
#     MxL_mass.append(mxl_kich)
#     print("\t",mxl_kich)
#     mxl_kich = []
# print(MxN_mass,"\t",MxL_mass)
# for x in range(0,len(MxL_mass)):
#     MxN_MxL = []
#     S = 0
#     for j in range(len(MxL_mass)):
#         P = 1
#         for b in range(len(MxN_mass)):
#             print(MxN_mass[m][b],MxL_mass[b][m])
N = int(input("N ="))
M = int(input("M ="))
L = int(input("L ="))
katta_mxn = []
for i in range(N):
    nxm = []
    for j in range(M):
        z = random.randint(1,4)
        nxm.append(z)
    print(nxm)
    katta_mxn.append(nxm)
katta_mxl = []
for k in range(M):
    mxl = []
    for l in range(L):
        a = random.randint(1,4)
        mxl.append(a)
    katta_mxl.append(mxl)
    print("\t",mxl)
for x in range(0,len(katta_mxl)):
    mat_Summ = []
    for m in range(len(katta_mxl)):
        S = 0
        P = 1
        for b in range(len(katta_mxn)):
            # print(katta_mxn[m][x],katta_mxl[x][b])
            P = katta_mxn[m][x] * katta_mxl[x][b] 
            S = S + P
            # print(S)
        mat_Summ.append(S)
        # # print(P)
        # # print(S)
    print(mat_Summ)
print(katta_mxn,"\t",katta_mxl)
# easdwdasdasd
# N = int(input("N ="))
# M = int(input("M ="))
# L = int(input("L ="))
# katta_mas_nxm = []
# for i in range(N):
#     nxm = []
#     for j in range(M):
#         z = random.randint(1,9)
#         nxm.append(z)
#     katta_mas_nxm.append(nxm)
#     print(nxm)
# mxl = []
# katta_mas_mxl = []
# for k in range(M):
#     for l in range(L):
#         r = random.randint(1,9)
#         mxl.append(r)
#     katta_mas_mxl.append(mxl)
#     print("\t",mxl)
#     # print(katta_mas_nxm,"\t",katta_mas_mxl)
#     mxl = []
# for m in range(len(katta_mas_mxl)):
#     maricha_Y = []
#     for n in range(len(katta_mas_mxl)):
#         S = 0
#         P = 1
#         for x in range(len(katta_mas_nxm)):
#             print(katta_mas_nxm[m][n])