# -*- coding: utf-8 -*-
#Løkken sjekker om brukeren taster inn et heltall. Gjentas til brukeren taster inn et heltall. 
while True:
    try:
        n=int(input("Hva er n?"))
    except ValueError:
        print("Dette er ikke et heltall! Prøv igjen")
    else:
        break

#Løkken sjekker om heltallet er større enn eller lik null. Gjentas til brukeren taster inn et gyldig heltall
while True:
    if n>0:
        break
    elif n==0:
        print("n fakultet er 1")
        break
    else:
        print("n må være større enn eller lik 0! Prøv igjen")
 
#Noen variabler for regning: n_org gjør så programmet har riktig startverdi av n i svaret. 
# a er en variabel for regning, og n_fak er n fakultet, altså det som skal bli svaret.     
n_org=n  
a=0
n_fak=1   
#Her begynner programmering for regningen
while True:
    n_fak=n_fak*(n-a) 
    if (n-a)==1:
        print(n_org, " fakultet er ", n_fak)
        break
    elif n==0:          #Programmet ble forvirret og fortsatte i uendelig løkke når n=0, så stopper løkken her
        break
    else:
        a+=1
    