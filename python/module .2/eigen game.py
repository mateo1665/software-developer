print('welkom bij de game castle.')
print('je moet zo snel naar het kasteel om het goud te pakken.')
naam = input("wat is je naam?")
print(f'welkom {naam} mijn naam is newcastle laten we naar het kasteel gaan we hebben haast.')
print('we zijn bijna bij de brug daar zullen we onze eerste vijanden tegen komen.')
print('we zijn bij de brug je ziet al trollen jou kracht is 5 als iemand minder is dan 5 dan vecht je hoger dan 5 ontwijken.')
gevecht_1 = input("2 trollen een van kracht 4 en een van kracht 7 wat moet je doen?")
if gevecht_1 == "vechten":
    print('goed bezig kom op laatste trol.')
    if gevecht_1 == 'ontwijken':
        print('lekker gedaan je hebt de 2 trollen verslagen!')
    else:
        ('je bent dood probeer het opnieuw.')
else:
    print('je bent dood probeer het opnieuw.')
print(f'lekker bezig {naam} laten we door gaan naar de deur want we moeten nog even.')
print('we zijn bij de deur dat zijn 2 grote trollen')
print('een van kracht 8 en 9 wat ga je doen?')
gevecht_2 = input("de twee trollen hebben een kracht van 8 en 9.")
if gevecht_2 == 'ontwijken':
    print('dat is een!')
    if gevecht_2 == 'ontwijken':
        print('goed gedaan je hebt de twee grote trollen verslagen!')
    else:
        print('je bent dood probeer het opnieuw.')
else:
    print('je bent dood probeer het opnieuw.') 
print('de deur is zwaar duwen!!')
print('de deur is open daar is de tovennaar!')
print('')