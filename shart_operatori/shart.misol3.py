X = int(input("X="))
Y = int(input('Y='))
Z = int(input('Z='))

a = X + Y + Z
b = X * Y * Z

if a > b:
    print(' a katta')
else:
    print('b katta')
#kichigi

A = ((X + Y + Z)/2)**2+1
B = ((X * Y * Z)**2)+1   

if A < B:
    print('A kichik')
else:
    print('B kichik')