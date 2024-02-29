A = float(input("A ="))
B = float(input("B ="))
C = float(input("C ="))
if A >= B >= C:
    print("qanoatlintiradi",A*2,B*2,C*2)
else:
    if A < 0:
        print(A * -1)
    else:
        print(A)
    if B < 0:
        print(B * -1)
    else:
        print(B)
    if C < 0:
        print(C * -1)
    else:
        print(C)
