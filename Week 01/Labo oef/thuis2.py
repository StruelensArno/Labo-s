#Schrijf een programma dat een kassasysteem nabootst.
#   Een broek kost 70,5 euro.
#   Een T-shirt kost 20,89 euro.
#   Een vest kost 100,3 euro.
#De gebruiker geeft per item het aantal gekochte goederen in. De computer berekent het te betalen bedrag.

prijs_broek= float(70.5)
prijs_tshirt= float(20.89)
prijs_vest= float(100.3)

print("*** Welkom bij het kassa systeem ***")
gekochte_broeken = int(input("Hoeveel broeken werden er gekocht? "))
gekochte_tshirts = int(input("Hoeveel T-shirts werden er gekocht? "))
gekochte_vesten = int(input("Hoeveel vesten werden er gekocht? "))
te_betalen = (prijs_broek * gekochte_broeken)+(prijs_tshirt*gekochte_tshirts)+(prijs_vest*gekochte_vesten)
print(f"totaal te betalen: \n {te_betalen}")