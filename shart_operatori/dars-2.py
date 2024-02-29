import math
x1=int(input("x1="))
y1=int(input("y1="))
x2=int(input("x2="))
y2=int(input("y2="))
x3=int(input("x3="))
y3=int(input("y3="))

A = math.sqrt(((x2-x1)**2)+(y2-y1)**2)

B = math.sqrt(((x3-x2)**2)+(y3-y2)**2)

C = math.sqrt(((x3-x1)**2)+(y3-y1)**2)

p=(A+B+C)/2

S = math.sqrt(p*(p-A)*(p-B)*(p-C))

print('A=', A , "B=", B, 'C=', C , "p=", p , "S", S)