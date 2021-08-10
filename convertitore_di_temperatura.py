#cpnertitore di temperatura kelvin,celsius,fahrenheit
titolo = '\n\n*****************CONVERTITORE DI TEMPERATURA*********************\n\n'
print(titolo.center(150))


gradi = int(input('grado che vuoi convertire== '))

menu = '***MENU***\n\n'
print(menu.center(150))

celsius_to_fahrenheit = '1.celsius to fahrenheit'
print(celsius_to_fahrenheit.center(150))

fahrenheit_to_celsius = '2.fahrenheit to celsius'
print(fahrenheit_to_celsius.center(150))

celsius_to_kelvin = '3.celsius to kelvin'
print(celsius_to_kelvin.center(150))

fahrenheit_to_kelvin = '3.fahrenheit to kelvin'
print(fahrenheit_to_kelvin.center(150))

kelvin_to_celsius = '4.kelvin to celsius'
print(kelvin_to_celsius.center(150))

kelvin_to_fahrenheit = '5.kelvin to fahrenheit\n\n'
print(kelvin_to_fahrenheit.center(150))

conversione = input("unita di misura da convertire= ")


if conversione == 'celsius to fahrenheit':
    risposta = (gradi * 9/5) + 32
    print("%.3f" % risposta + str('°F'))

if conversione == 'fahrenheit to celsius':
    risposta1 = (gradi-32) * 5/9
    print("%.3f" % risposta1 + str('°C'))

if conversione == 'celsius to kelvin':
    risposta2 = gradi + 273.15
    print("%.3f"  % risposta2 + str('K'))

if conversione == 'fahrenheit to kelvin':
    risposta3 = (gradi-32) * 5/9 + 273.15
    print("%.3f" % risposta3 + str('K'))

if conversione == 'kelvin to celsius':
    risposta4 = gradi - 273.15
    print("%.3f"  % risposta4 + str('°C'))

if conversione == 'kelvin to fahrenheit':
    risposta5 = (gradi-273.15) * 9/5 + 32
    print("%.3f"  % risposta5 + str('°F'))


