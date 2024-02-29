a = float(input('olma kg='))
b = float(input('anor kg='))

olma = 5000
anor = 6000

if a >= 3 and a < 5: 
    a_skidka = 10
elif a >= 5 and a < 10:
    a_skidka = 20
elif a >= 10:
    a_skidka = 30
else:
    a_skidka = 0
if b >= 5:
    b_skidka = 10
else:
    b_skidka = 0

a_summ = olma * a 
a_skidka_a = a_summ * (100-a_skidka) / 100

b_summ = anor * b
b_skidka_b = b_summ * (100-b_skidka) / 100


print( 

)