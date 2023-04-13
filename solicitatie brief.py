# solicitatie van Mateo
# de vragen die worden gesteld bij de solicitatie
naam = input("wat is je naam? ")
print(f"welkom bij het gesprek {naam}")
geslacht = input("wat is uw geslacht is dat een man of vrouw")
if geslacht == 'man':
    snor = input("heeft u een snor? ")
    if snor == 'ja':
        grootte_snor = int(input("wat is de grootte van uw snor? "))
elif geslacht == 'vrouw':
    haarkleur = input("heeft u een haarkleur")
    if haarkleur == 'ja':
        grootte_haar = int(input("wat is de grootte van uw haar? "))
diploma = input("heeft u een MBO-4 diploma? ")
rijbewijs_vrachtwagen = input("heb je een rijbewijs voor vrachtwagens? ")
hoed = input("heeft u een grote hoed? ")
lengte = int(input("wat is uw lengte? "))
gewicht = int(input("hoe zwaar bent u? "))
certificaat = input("heb je een certificaat met overleven met gevaarlijk personeel? ")
praktijkervaring = int(input("hoelang heb je een ervaring met het dierendessuur "))
jongleren = int(input("hoelang heb je ervaring met jongleren? "))
acrobatiek = int(input("hoelang heb je ervaring met acrobatiek? "))

# hier geeft de if en else aan of je bent aangenomen ja of nee
if naam == 'ja' and ((geslacht == 'man' and snor == 'ja' and grootte_snor > 10) or (geslacht == 'vrouw' and haarkleur == 'ja' and grootte_haar > 20)) and diploma == 'ja' and rijbewijs_vrachtwagen == 'ja' and hoed == 'ja' and lengte > 150 and lengte < 220 and gewicht > 90 and gewicht < 120 and certificaat == 'ja' and praktijkervaring >= 4 and jongleren >= 5 and acrobatiek >= 3:
    print('u bent aangenomen voor de baan')
else:
    print('u bent niet geschikt voor deze baan')