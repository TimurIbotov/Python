from math import*
A = int(input("A ="))
B = int(input("B ="))
C = int(input("C ="))
if A == 0:
    print("Chiziqli teglama")
else:
    D = B ** 2 -4 * A * C
    if D < 0:
        print("Yechimga ega emas")
    elif D == 0:
        X1 =-B / 2 * A
        print(X1)
    else:
        X1 = (-B + sqrt(D)) / (2 * A)
        X2 = (-B + sqrt(D)) / (2 * A)
        print(X1,X2)