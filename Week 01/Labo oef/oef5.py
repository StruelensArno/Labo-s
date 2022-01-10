#Vraag aan de gebruiker het aantal dagen, uren, minuten en seconden op.
#Bepaal het totale aantal seconden.

#inlezen
#het =-teken kan je lezen als WORDT
dagen = int(input("geef het aantal dagen op: "))
uren = int(input("geef het aantal uren op: "))
minuten = int(input("geef het aantal minuten op: "))
seconden = int(input("geef het aantal seconden op: "))

#berekening
totaal_sec = (seconden+(minuten*60)+(uren*3600)+(dagen*24*3600))

#resultaat
print(f"Het totale aantal seconden bedraagt: {totaal_sec}")
