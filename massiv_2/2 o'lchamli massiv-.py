# N = int(input("N ="))
# qadam = 0
# for i in range(0,7):
#     for j in range(0,7):
#         for k in range(0,7):
#             for L in range(0,7):
#                 for M in range(0,7):
#                     qadam += 1
#                     if (i == 1) and (j == 4) and (k == 3) and (L == 2) and (M == 2):
#                         print( i ,j , k, L , M)
#                         print(qadam)
#                         break
def faktion(c):
    B = []
    a = []
    for i in range(c):
        for j in range(c):
            a.append(0)
        B.append(a)
        a=[]
    return(B)
N= int(input("N ="))
x = faktion(N)
print(x)
