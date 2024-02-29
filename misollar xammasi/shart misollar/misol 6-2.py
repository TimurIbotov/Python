x = int(input("x ="))
y = int(input("y ="))
z = int(input("z ="))
if x > y > z:
    print("x katta",x)
elif y > z:
    print("y katta",y)
elif z > y:
    print("z katta", z)
else:
    print("xammasi teng")
    # KICHIK MIN
# elif x < y < z:
#     print("x kichik", x)
# elif y < z:
#     print('y kichik',y)
# elif z < y:
#     print("z kichik", z)
# else:
# print("xammasi teng")