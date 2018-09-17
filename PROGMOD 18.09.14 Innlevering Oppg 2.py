# -*- coding: utf-8 -*-
#Trenger å bruke math.sqrt senere, så importerer matte her
import math
#Startbeskjed, forklarer programmet for brukeren
print("Dette programmet kan bruke formelen for kinetisk energi for et legeme i bevegelse.")
print("Hvis du har to av variablene, kan programmet finne den siste.")

#Spør etter variabelen man vil finne her
var=input("Hvilken variabel vil du finne? E (energi), m (masse) eller v (fart)?")

#Lager en liste her, så hvilken variabel man vil ha blir riktig oppfattet, input kan skrives på flere måter
E=["E", "e", " E", " e", "energi", "Energi", " energi", " Energi"]
m=["m", "M", " m", " M", "masse", "Masse", " masse", " Masse"]
v=["v", "V", " v", " V", "fart", "Fart", " fart", " Fart"]

#Beregning starter her, en "if" for hver variabel man vil finne
if var in E:                                                #Finner Energi
    print("Så du vil finne den kinetiske energien!")         #Forteller brukeren at programmet har skjønt hvilken variabel de skal finne
    var_m=float(input("Hva er m (massen) i kg?"))
    var_v=float(input("Hva er v (farten) i m/s?"))
    svar_E=0.5*var_m*(var_v**2)                                    #Regner ut kinetisk energi
    print("Den kinetiske energien er E= ", str(svar_E), " J.")     #Gir brukeren svaret
    
elif var in m:                          #Finner masse
    print("Så du vil finne massen!")     #Forteller brukeren at programmet har skjønt hvilken variabel de skal finne
    var_E=float(input("Hva er E (energien) i J?"))
    var_v=float(input("Hva er v (farten) i m/s?"))
    svar_m=(2*var_E)/(var_v**2)                         #Regner ut massen
    print("Massen er ", svar_m, " kg.")                 #Gir brukeren svaret
    
elif var in v:                          #Finner fart
    print("Så du vil finne farten!")     #Forteller brukeren at programmet har skjønt hvilken variabel de skal finne
    var_E=float(input("Hva er E (energien) i J?"))
    var_m=float(input("Hva er m (massen) i kg?"))
    svar_v=math.sqrt((2*var_E)/var_m)                   #Regner ut farten
    print("Farten er ", svar_v, " m/s.")                #Gir brukeren svaret
    
else:
    print("Oi da, her skjedde det noe feil - jeg skjønte ikke hvilken variabel du skulle frem til. Prøv igjen, og svar 'E', 'm' eller 'v'!")
