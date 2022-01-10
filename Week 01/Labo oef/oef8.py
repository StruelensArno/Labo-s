#Vraag aan de gebruiker twee int-getallen (gehele getallen) op.
#Bereken nu volgend resultaat: (x + y) * (x + y).

#inlezen
x = int(input("geef een getal op: "))
y = int(input("geef een getal op: "))
#berekenen
#met ** kan je een macht berekenen

#optie 1
berekening= (x+y) * (x+y)

#optie 2 
#berekening= (x+y)**2

#resultaat
print(f'( {x} + {y} ) ^2) ={berekening}')