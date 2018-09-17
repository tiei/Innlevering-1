# -*- coding: utf-8 -*-
#Forklarer programmet til brukeren:
print("Dette programmet kan regne ut en bestand av dyr etter et bestemt antall år, hvis du vet endringsprosenten og nåværende bestand")
endring = input("Synker eller vokser bestanden?")       #Det første brukeren ser - bestemmer hvilken "if"
synker=["Synker", " Synker", "synker", " synker", "Den synker", "Bestanden synker"]  #Lister, så flere måter å skrive 'synker' og 'vokser' forstås
vokser=["Vokser", " Vokser", "vokser", " vokser", "Den vokser", "Bestanden vokser"]


if endring in synker:
    Bnå=int(input("Hva er den nåverende bestanden?"))                           #Finner variablene programmet trenger for å regne ut bestanden
    p=float(input("Hvor mange prosent synker bestanden med per år?"))
    t=float(input("Hvor mange år fra i dag vil du vite hva bestanden er?"))             #Setter r=1 for å ha en variabel som kan 'avbryte' løkken
    r=1
    while r<=t:
          Bny=(Bnå*(1-(p/100)))
          Bnå=Bny
          r+=1
    print("Bestanden etter ", t, "år, er ", int(Bny), "individer")          #Output
                
    
elif endring in vokser:
    Bnå=int(input("Hva er den nåværende bestanden?"))                           #Finner variablene programmet trenger for å regne ut bestanden
    p=float(input("Hvor mange prosent vokser bestanden med per år?"))
    t=float(input("Hvor mange år fra i dag vil du vite hva bestanden er?"))             #Setter r=1 for å ha en variabel som kan 'avbryte' løkken
    r=1
    while r<=t:
        Bny=(Bnå*(1+(p/100)))
        Bnå=Bny
        r+=1
    print("Bestanden etter ", t, "år, er ", int(Bny), "individer")          #Output
    

    
else:
    print("Oi da, jeg skjønte ikke hva du skrev. Prøv igjen!")              #Feilmelding hvis programmet ikke skjønner svaret fra første input
    
    

