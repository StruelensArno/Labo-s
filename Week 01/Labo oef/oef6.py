#Vraag aan de gebruiker een aantal seconden op.
#Zet dit aantal om in dagen, uren, minuten en seconden.

#inlezen
sec = int(input("geef het aantal seconden op: "))

#berekening
#modulo berekent (normaal gezien/afhankelijk hoe je het gebruikt) de rest --> teken voor modulo is %
#gehele deling zal alles die na de komma staat gewoon weggooien --> symbool voor geheel delen is //
dagen = sec // (24*3600)
rest = sec % (24*3600)

uren = rest // 3600
rest = rest % 3600

minuten = rest //3600
rest = rest //60

seconden = rest %60

#resultaat tonen
print(f"d:h:m:s -> {dagen}:{uren}:{minuten}:{seconden}")