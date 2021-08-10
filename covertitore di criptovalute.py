titolo = 'CONVERTITORE DI CRIPTOVALUTE IN DOLLARI\n\n'
print(titolo.center(150))

print('ricordiamo che 1btc = 44952,60$\n\n')
print('ricordiamo che 1eth = 3085.85$\n\n')
print('ricordiamo che 1usdt = 1.0003$\n\n')
print('ricordiamo che 1bnb = 370,32$\n\n')

risposta = input('cosa voui convertire? \n\n')

if risposta == 'bitcoin in dollari':
    bitcoin = int(input('numero di bitcoin che vuoi convertire in dollari '))
    ris = bitcoin * 44952.60
    print('risultato == ' + str(ris) + str('$'))

if risposta == 'dollari in bitcoin':
    dollaro = int(input('numero di dollari che vuoi conventire in bitcoin '))
    ris = dollaro/44952.60
    print('risultato == ' + str(ris) + str('BTC'))

if risposta == 'etherium in dollari':
    etherium = int(input('numero di etherium che vuoi convertire in dollari '))
    ris = etherium * 3132.86
    print('risultato == ' + str(ris) + str('$'))

if risposta == 'dollari in etherium':
    dollaro = int(input('numero di dollari che vuoi conventire in etherium'))
    ris = dollaro/3132.86
    print('risultato == ' + str(ris) + str('ETH'))

if risposta == 'tether in dollari':
    tether = int(input('numero di tether che vuoi convertire in dollari '))
    ris = tether * 1
    print('risultato == ' + str(ris) + str('$'))

if risposta == 'dollari in tether':
    dollaro = int(input('numero di dollari che vuoi conventire in tether'))
    ris = dollaro/1
    print('risultato == ' + str(ris) + str('USDT'))

if risposta == 'binance coin in dollari':
    binance_coin = int(input('numero di binance coin che vuoi convertire in dollari '))
    ris = binance_coin * 370.54
    print('risultato == ' + str(ris) + str('$'))

if risposta == 'dollari in binance coin':
    dollaro = int(input('numero di dollari che vuoi conventire in binance coin'))
    ris = dollaro/370.54
    print('risultato == ' + str(ris) + str('BNB'))