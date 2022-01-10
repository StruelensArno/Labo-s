#Vraag aan de gebruiker een int-getal n op. Bereken de volgende som: n + nn + nnn.
#Print het resultaat af.

#inlezen
n=int(input("geef een getal op: "))

#berekenen
resultaat= n + (n*11) + (n*111)
#Optie 2
#!bij inlezen de input niet gedifineert worden als int
#resultaat= int(n) + int(n+n) + int(n+n+n)

#optie 3
#!bij inlezen de input niet gedifineert worden als int
#resultaat = int(n) + int((n*2)) + int((n*3))

#resultaat
print(f"het resultaat is: {resultaat}")