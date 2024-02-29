# N = int(input("N ="))
# birlik = {
#     1 : "Bir",
#     2 : "ikki",
#     3 : "uch",
#     4 : "to'rt",
#     5 : "besh",
#     6 : "olti",
#     7 : "yetti",
#     8 : "sakkiz",
#     9 : "to'qqiz",
#     0 : " ",
#     }
# unlik = {
#     1 : "O'n",
#     2 : "yigirma",
#     3 : "o'ttiz",
#     4 : "qirq",
#     5 : "ellik",
#     6 : "oltmish",
#     7 : "yetmish",
#     8 : "sakson",
#     9 : "to'qson",
#     }
# y_m = {
#     1 : "yuz",
#     2 : "ming",
#     }
# suz = str(N)
# suz2 = len(str(N))
# chiqarish = 0
# if suz2 == 1 :
#     chiqarish = birlik(N)
# elif suz2 == 2 :
#     chiqarish = unlik[int(suz[0])] +' ' + birlik[int(suz[1])]
# elif suz2 == 3 :
#     chiqarish = birlik[int(suz[1])] +' ' + y_m[int(suz[0])] +' ' + unlik[int(suz[1])] +' ' + birlik[int(suz[1])]
# print(chiqarish)

# suz = str(N)
# chiqarish = unlik[int(suz[0])] +' ' + birlik[int(suz[1])]
# print(chiqarish)
# yuzlik = {
#     1 : "Yuz",
#     2 : "Ikki yuz",
#     3 : "Uch yuz",
#     4 : "To'rt yuz",
#     5 : "Besh yuz",
#     6 : "Olti yuz",
#     7 : "Yetti yuz",
#     8 : "Sakkiz yuz",
#     9 : "To'qqiz yuz",
# }
# qq = str(N)
# yuzlik = yuzlik[int(suz[0])] +' ' + unlik[int(suz[1])] +' ' + birlik[int(suz[2])]
# print(yuzlik)
# minglik = {
#     1 : "ming",
#     2 : "ikki ming",
#     3 : "uch ming",
#     4 : "to'rt ming",
#     5 : "besh ming",
#     6 : "olti ming",
#     7 : "yetti ming",
#     8 : "sakkiz ming",
#     9 : "to'qqiz ming",
#     }
# ming = str(N)
# summ = minglik[int(ming[0])] +' ' + yuzlik[int(suz(1))] + ' '+ unlik[int(suz[2])] +' ' + birlik[int(suz[3])]
# print(ming)