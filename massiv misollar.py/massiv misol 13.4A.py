# N = int(input("N ="))
# z = 0
# a = [7,1,6,10,15,16,9]
# b = []

# for i in range(1,len(a)):
#     print(a)
#     q = min(a)
#     b.append(q)
#     print(b)
import random
N = int(input("N ="))
z = 0 
a = []
S = 0
for i in range(1, N+1):
    z = random.randint(-5,N)
    a.append(z)
print(a)
for j in a:
    if j > 0:
        S = S + j
    elif j <= -1:
        break
print(S)

# i = 0
# while i <= len(a):
#     print(a)
#     q = min(a)
#     b.append(q)
#     print(b)
#     a.pop(1)
#     i += 1
# for x in a:
#     b = min(a)
#     print(b)