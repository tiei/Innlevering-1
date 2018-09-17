# -*- coding: utf-8 -*-
import math     #Må bruke matte for å regne med log, så importerer her

#Variablene mine er her:
ioner=float(input("Hva er antallet H+-ioner i mol per liter?")) # Input, H+-ioner 
pH=(-1)*math.log10(ioner)             #Utregning av pH, fra input 
pHverdi="pH-verdien er "+ str(pH)             #For å slippe å skrive samme tekst flere ganger i if/else under

if 0<=pH<7:                          #For sur løsning
    print(pHverdi)                              
    print("Løsningen er sur")
elif pH==7:                          #For nøytral løsning
    print(pHverdi)
    print("Løsningen er nøytral")
elif 7<pH<=14:                       #For basisk løsning               
    print(pHverdi)
    print("Løsningen er basisk")
else:                                #Feilmelding - hvis svaret ikke ligger innen pH-skalaen fra 0 til 14
    print("Her må det ha skjedd noe feil - prøv igjen!")
    
   