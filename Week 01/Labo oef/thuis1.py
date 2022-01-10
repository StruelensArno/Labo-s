#Om de prijs van een woning te bepalen, telt men de prijs van de bouwgrond en de eigenlijke bouw op.
#Het btw-tarief op dit totaal is 21 %.
#Je vraagt aan de gebruiker de prijs van de bouwgrond en de prijs van het gebouw.
#Je toont het totaal te betalen bedrag.

#inlezen
prijs_bouwgrond = float(input("prijs van de bouwgrond? "))
prijs_gebouw = float(input("prijs van het gebouw? "))

#berekening
btw = (prijs_bouwgrond+prijs_gebouw)* 1.21

#resultaat
print(f"de totale kostprijs van het project: {btw}")