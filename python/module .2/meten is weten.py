# meten is weten Mateo Vukoje
#input en if statement
a = int(input('a getal'))
b = int(input('b getal'))

if a > b:
    print('a is een groter getal dan b')
    a = max
elif a < b:
    print('b is een groter getal dan a')
    b = max

print('----------')
#elif statement
a = int(input('a getal'))
b = int(input('b getal'))

if a > b:
    print('b is een kleiner getal dan a')
elif a < b:
    print('a is een kleiner getal dan b')

print('----------')
#else statement
if a > b:
    print('b is een kleiner getal dan a')
else:
    print('getal a en getal b zijn even groot')

print('----------')
#min en max
print('Het minimum is: ’ gevolgd door de waarde van Min')
print('Het maximum is: ’ gevolgd door de waarde van Max')