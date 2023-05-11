#de pizza calculator van Mateo Vukoje
# de vraag naar hoeveel pizzas
small = int(input(f'hoeveel small pizzas wil je? '))
medium = int(input(f'hoeveel medium pizzas wil je? '))
large = int(input(f'hoeveel large pizzas wil je? '))

# de berekening van de pizzas
# het bonnetje 
print('----------')
print('bonnetje van uw bestelling')
print('')
print(f'small pizzas {small} de totaal prijs van de small pizzas' ,small * 5.99,)
print(f'medium pizzas {medium} de totaal prijs van de medium pizzas' ,medium * 8.99,)
print(f'large pizzas {large} de totall prijs van de large pizzas',large * 13.99,)
print('----------')
print('de prijs',small * 5.99 + medium * 8.99 + large * 13.99,)