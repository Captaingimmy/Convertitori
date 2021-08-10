#convertitore peso-newton,newton peso
#ricordiamoci che un 1kg corrisponde a 9,81N

titolo = '************CONVERTITORE PESO-NEWTON,NEWTON-PESO*************\n\n'
print(titolo.center(150))

menu = '****MENU****\n\n'
print(menu.center(150))
newton = 'newton-peso'
peso = 'peso-newton'
print(newton.center(150))
print(peso.center(150))

domanda1 = input('che equivalenza vuoi fare? ')

if domanda1 == newton:
   newton_do = int(input('dimmi la misura in newton\n'))
   risposta = newton_do / 9.81
   print(risposta)

if domanda1 == peso:
   peso_do = int(input('dimmi la misura in kg\n'))
   risposta = peso_do * 9.81
   print(risposta)

