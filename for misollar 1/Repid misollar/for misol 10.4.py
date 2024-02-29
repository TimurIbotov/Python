# N = int(input("N ="))
# V = 0
# S = 0
# P = 1
# if N < 3:
#     V1 , V2 = 0 , 0
#     print("V1", V1 , "V2", V2)
# elif N == 3:
#     V3 = 1.5
#     print("V3 =", V3)
# if N <= 4:
#     for i in range(4, N +1):
#         v1, v2 = 0 , 0
#         v3 = 1.5
#         S = (i + 1) / ((i**2)+1) * v3 - v2 * v1
# print("S", S)
N = int(input("N ="))
V1 , V2 = 0 , 0
V3 = 1.5
if N >= 4:
    for i in range(4, N + 1):
        V4 = ((i + 1) / ((i**2) + 1)) * V3 - V2 * V1
        V1 = V2
        V2 = V3
        V3 = V4
    print("V4", V4)
else:
    print("Kechirasiz")





# for i in range(4, N+1):
#     if N < 3:
#         V = 0
#     elif N == 3:
#         V == 1.5
#     elif N >= 4:
#         v1i = i - 1
#         v2i = i - 2
#         v3i = i - 3
#         V = (i + 1) / ((i**2)+1)*v1i - v2i * v3i
# print("V =", V)