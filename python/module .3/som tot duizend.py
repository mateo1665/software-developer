begin_getal = 50
som = 50
zin = '50'
while som < 1000:
    begin_getal += 1
    som = som + begin_getal
    zin += (f'+ {begin_getal}')
    print(f'{zin} = {som}')