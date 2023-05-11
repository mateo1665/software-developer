#de pizza calculator van Mateo Vukoje
# de vraag naar hoeveel pizzas
small = 5.99
medium = 8.99
large = 13.99

small = input('wil je een small pizza? ')
if small == "ja":
    print('oke')
    small = int(input('hoeveel small pizzas wilt u? '))
elif small == "nee":
    print('is goed')
else:
    print('ik begrijp u niet')
medium = input('wil je een medium pizza')
if medium == "ja":
    print('oke')
    medium = int(input('hoeveel medium pizzas wilt u? '))
elif medium == "nee":
    print('is goed')
else:
    print('ik begrijp u niet')
large = input('wilt u een large pizza? ')
if large == "ja":
    print('oke')
    large = int(input('hoeveel large pizzas wilt u? '))
elif large == "nee":
    print('is goed')
else:
    print('ik begrijp u niet.')

# de berekening van de pizzas
# het bonnetje 
print('----------')
print('bonnetje van uw bestelling')
print('')
print(f'small pizzas {small} de totaal prijs van de small pizzas')
print(f'medium pizzas {medium} de totaal prijs van de medium pizzas' )
print(f'large pizzas {large} de totall prijs van de large pizzas' )
print('----------')
print(small * 5.99 + medium * 8.99 + large * 13.99)