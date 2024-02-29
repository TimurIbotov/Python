
# a = "Hellow world"
# print(a.upper()) # xarflarni xammasini katta kilib beradi
# b = "Hellow, World"
# print(b.lower()) # sonlarni mayda kilib beradi
# c = "Hellow, World"
# print(c.strip()) # Bo'sh kataklarni tawlab ketadi
# g = "Hellow, World"
# print(g.replace("H", "J")) #Xarflrani joyini o'rgatadi
# A = "Hellow, World"
# print(A.split(",")) # satrni pastki qatorlarga ajratadi
# age = 36 
# txt = "My name is John, and I am {}"
# print(txt.format(age)) # Satrga kritish
# a = ["apple", 'banana', 'cherry']
# a[1] = "blackcurrant"
# print(a)
B = ["apple", "banana", "cherry", "orange", "kiwi", "mango",]
B [1:3] = ["blackcurrant", "watermelon"]
print(B)
C = ["apple", "banana", "cherry"]
C [1:2] = ["blackcurrant", "watermelon"]
print(C)
G = ['apple','banana','cherry']
G[1:3] = ["watermelon"]
print(G)
X = ["apple", "banana","cherry"]
X.insert(2,"watermelon")
print(X)
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
t = ["apple", "banana", "cherry"]
t.insert(1, "orange")
print(t)
i = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
i.extend(tropical)
print(i)
h = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
h.extend(thistuple)
print(h)
s = ["apple", "banana", "cherry"]
s.remove("banana")
print(s)
l = ["apple", "banana", "cherry"]
l.pop(1)
print(l)
u = ["apple", "banana", "cherry"]
u.pop()
print(u)

o = ["apple", "banana", "cherry"]
del o[0]
print(o)

p = ["apple", "banana", "cherry"]
p.clear()
print(p)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


 # A BOR SO'ZLARNI CHIKORIB BERADI

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# # newlist = [x for x in fruits if "a" in x]
# # newlist = [x for x in range(10) if x < 5] 

# # newlist = [x.upper() for x in fruits] 
# # newlist = ['hello' for x in fruits] 
# # newlist = [x if x != "banana" else "orange" for x in fruits]
# # newlist = [x for x in range(10)]
# print(newlist)

# newlist = [x for x in fruits if x != "apple"] 


 #SARTIROVKA KILIB BERADI
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)
# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist)
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) 

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
# CHAPACHASIGA TASHAYDI
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


#append() Listga elemnt Qo'shih
# clear () LISTNI TOZALASH
# copy () RO'YXATNI NUSXASINI YARATISH
# count () LIST ICHIDAGI ELEMENTLARNI SANASH
# extend () LIST1 NI OXIRIGA LIST2 NI QO'SHISH
# index () 
# insert () XOXLAGAN INDEKSIMIZDA ELEMENT QO'SHIH
# pop () ELEMENTNI 
# remove ()