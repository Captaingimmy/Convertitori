#questo programma si basa su come si calcola una percentuale 
#questo programma sara un calcolatore di percentuale

print("********CALCOLATORE DI PERCENTUALE********\n")

prezzo = int(input("inserisci il prezzo del prodotto== "))

sconto = int(input("dimmi la precentuale dello sconto== "))

#print(sconto + "%" + "di" + prezzo)

risposta = input("vuoi calcolare la percentuale:")

if risposta == "si":
   percentuale = prezzo*sconto/100
   print("percentale calcolata == " + str(percentuale))

if risposta == "no":
   print("\nARRIVEDERCI alla prossima")
