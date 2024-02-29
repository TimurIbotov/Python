x = float(input("x ="))
N = 8
a = (x ** 2) + (2 ** N) / x ** 2
for i in range(1, N):
     S = N - i
     a = (x ** 2) + (2 ** S) / a
print("a =", 1/a)