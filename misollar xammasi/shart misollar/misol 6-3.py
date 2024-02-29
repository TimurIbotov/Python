X = int(input("X ="))
Y = int(input("Y ="))
Z = int(input("Z ="))
S = X + Y + Z / 2
P = X * Y * Z
   # MAX
# if S > P:
#     print("S katta", S)
# else:
#     print("P katta", P)
if S < P:
    print("S kichik", S**2 + 1)
else:
    print("P kichik", P ** 2 + 1)

print(S)
print(P)
