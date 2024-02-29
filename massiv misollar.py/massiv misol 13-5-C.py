import random
N = int(input("N ="))
z = 0
a = []
max = 0
for i in range(1,N+1,):
    z = random.randint(1,N)
    a.append(z)
for j in range(0,len(a),2):
    if max < a[j]:
        max = a[j]
print(a)
print(max)