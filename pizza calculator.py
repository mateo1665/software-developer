# pizza cslculator van Mateo
small = 1
medium = 1
large = 1
smallprijs = 5.99
mediumprijs = 8.99
largeprijs = 13.99


groottepizza = input("wat voor grootte wil je je pizza hebben? ")
if groottepizza == "small" :
    print('de small versie van de pizza. ')
    hoeveelsmall = input("hoeveel smalle pizzas wil je? ")
    print(f'je wil dus {hoeveelsmall} smalle pizzas. dat ')
elif groottepizza == "meduim":
    print('de meduim versie van de pizza. ')
    hoeveelmeduim = input("hoeveel meduim pizzas wil je? ")
    print(f'je wil dus {hoeveelmeduim} meduim pizzas. ')
elif groottepizza == "large":
    print('de large versie van de pizza. ')
    hoeveellarge = input("hoeveel large pizzas wil je hebben? ")
    print(f'je wil dus {hoeveellarge} large pizzas. ')

print('-------------')
print('bonnetje')
print('')