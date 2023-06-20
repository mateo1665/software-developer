# name of student: mateo vukoje
# number of student: 9907255
# purpose of program: 
# function of program: 
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # hoeveel je moet betalen
paid = int(float(input('Paid amount: ')) * 100) # hoeveel je betaald hebt
change = paid - toPay # wisseln is betaald min hoeveel je hebt betaald

if change > 0: # als je wisselt 
  coinValue = 50 # is de waarde van de coin 50 
  
  while change > 0 and coinValue > 0: # blijft door met wisselen tot nu en de waarde van de coin daarvan
    nrCoins = change // coinValue # aantal coins is het wisselen delen van de waarde van de coin

    if nrCoins > 0: # als de aantan nummer coins groter is dan 0
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # wordt er geprint met maximal wat je terug krijgt aantal coins van de waarde van de coins in centen
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #nummer coins die je terug krijgt en dat typ je in hoeveel waarde je hebt terug gekregen in centen
      change -= nrCoinsReturned * coinValue # wisselen min het aantal coins wat je hebt terug gekregen keer het waarde van de coin

# comment on code below: 
    if coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # als de wissel groter is dan nul als wissel niet is gereturnd dan wissel het in cents zowel dan is het klaar
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')