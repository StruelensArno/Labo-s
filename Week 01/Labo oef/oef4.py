#Vraag aan de gebruiker de basis en de hoogte van een driehoek op.
#Bereken nadien de oppervlakte en print deze nadien af.

#inlezen
basis = float (input('Geef de basis van de driehoek op: '))
hoogte = float (input('Geef de hoogte van de driehoek op: '))

#berekenen
opp = (basis * hoogte)/2

#resultaat tonen
# .2f toont 2 cijfers na de komma (!!niet afgerond!!) Vergeet de f niet!
print(f"De oppervlakte bedraagt: {opp:.2f}")
