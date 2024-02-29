X = int(input("X="))
Y = int(input('Y='))
Z = int(input('Z='))

if X > Y > Z:
    print('X katta')
elif X > Z:
    print('X katta')
elif Y > Z:
    print('Y katta')
else:
    print('Z katta')
# Kichigi
if X < Y < Z:
    print('X kichik')
elif X < Z:
    print('X kichik')
elif Y < Z:
    print('Y kichik')
else:
    print('z kichik')