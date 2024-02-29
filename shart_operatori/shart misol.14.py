from math import*

a = float(input('a='))
b = float(input('b='))
c = float(input('c='))

if a == 0:
    print('Chizigli tenglama')
    # D = pow(b*2) - 4 * a * c
    # X3 = ((-b) / (2 * a))
    # X1 = ((-b + sqrt(D))/ (2 * a))
    # X2 = ((-b - sqrt(D)) / (2 * a))
else:
    D = pow(b,2) - 4 * a * c

    if D < 0:
        print('Yechimga ega emas')
    elif D == 0:
        X3 = (-b)/(2 * a)
        print("X3=", X3)
    else:
        X1 = ((-b + sqrt(D)) / (2 * a))
        X2 = ((-b - sqrt(D))/ (2 * a))
        print('X1=', X1, 'X2=', X2, )
    # else:
    #     X1 = ((-b + sqrt(D)) / (2 * a))
    #     X2 = ((-b - sqrt(D))/ (2 * a))
        