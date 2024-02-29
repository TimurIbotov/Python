import random
# N = int(input("N ="))
# z = 0
# m = []
# for i in range(1,N+1):
#     z = random.randint(0,N)
#     m.append(z)
#     a = max(m)
# print("a =", a)
# print("M =", m)
N = int(input("N ="))
z = 0 
m = []
max = 0
for i in range(1,N+1):
    z = random.randint(0,N)
    m.append(z)
    if max < z:
        max = z
print("max =", max)
print("M =", m)