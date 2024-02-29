import random
N = int(input("N ="))
z = 0
a = []
min = N
for i in range(1,N+1,):
    z = random.randint(1,N)
    a.append(z)
for j in range(1,len(a),1):
    if min > a[j]:
        min = a[j]
print(min)
print(a)