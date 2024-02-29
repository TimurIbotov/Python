d = int(input("d ="))
c = int(input("c ="))
b = int(input("b ="))
a = int(input("a ="))
if d >= c >= b >= a:
    print(d,d,d,d)
elif a > b > c > d:
    print("a =", a, "b =", b , "c =", c , "d =", d)
else:
    print("a =", a ** 2, "b =", b ** 2,"c =", c ** 2, "d =", d ** 2)