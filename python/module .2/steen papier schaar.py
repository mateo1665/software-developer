import random 
keuzes = ['r','s','p','t']
keuze_bedoeling = {
    'r': 'rock',
    's': 'sissors',
    'p': 'paper',
    't': 'tafel'
}
moeilijkheid = input('welke moeilijkheid wil je hebben: ')
if moeilijkheid == 'onmogelijk':
   print('je speelt nu tegen een god')
else:
   print('je speelt op normaal ')
   keuze_computer = random.choice(keuzes)
   print(keuze_computer)

countermoves = []
speler_keuze = input("wat kies je r = rock s = sissors p = paper t = tafel.")
if moeilijkheid == 'onmogelijk':
   if speler_keuze == 'r':
      keuze_computer = 'p'
   elif speler_keuze == 'p':
      keuze_computer = 's'
   elif speler_keuze == 's':
      keuze_computer = 'r'
   elif speler_keuze == 't':
      keuze_computer = 's'

if speler_keuze in keuzes:
   print(f'jouw keuze {keuze_bedoeling[speler_keuze]}. keuze van de computer {keuze_bedoeling[keuze_computer]}.')
   if (speler_keuze == keuze_computer) or (speler_keuze == 't' and keuze_computer == 'r'):
      print('gelijkspel')
   elif (speler_keuze == 'r' and keuze_computer == 's') or (speler_keuze == 's' and keuze_computer == 'p') or (speler_keuze == 'p' and keuze_computer == 'r') or (speler_keuze == 't' and keuze_computer == 'p'):
       print('je hebt gewonnen ')
   else:
      print('je hebt verloren sorry volgende keer beter')
else:
   print('sorry ik begrijp je niet')

