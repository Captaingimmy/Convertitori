#convertitore di valute con while
titolo = 'CONVERTITORE DI VALUTE\n'
print(titolo.center(150))

menu = 'MENU'
print(menu.center(150))
euro_to_dollars = '1.euros to dollars'
print(euro_to_dollars.center(150))
dollars_to_euros= '2.dollars to euros'
print(dollars_to_euros.center(150))
exit = '3.exit'
print(exit.center(150))


trovato = True

while trovato:
    risposta = input('dimmi che valuta vuoi convertire in? ')
    Trovato = True
    if risposta == 'euros to dollars':
        ris = int(input('euro da convertire in dollari== '))
        risultato = ris * 1.17
        print('risultato == ' + str(risultato) + str(' $'))
    if risposta == 'dollars to euros':
        ris = int(input('dollari da convertire in euro== '))
        risultato = ris*0.85
        print('risultato == ' + str(risultato) + str(' €'))
    
    if risposta == 'exit':
        trovato = False
