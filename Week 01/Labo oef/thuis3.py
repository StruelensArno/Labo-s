#Pas de uitvoer van thuis2 als volgt aan (let op het inspringen en de spaties): (zie pdf)

prijs_broek= float(70.5)
prijs_tshirt= float(20.89)
prijs_vest= float(100.3)

print("*** Welkom bij het kassa systeem ***")
gekochte_broeken = int(input("Hoeveel broeken werden er gekocht? "))
gekochte_tshirts = int(input("Hoeveel T-shirts werden er gekocht? "))
gekochte_vesten = int(input("Hoeveel vesten werden er gekocht? "))
te_betalen = (prijs_broek * gekochte_broeken)+(prijs_tshirt*gekochte_tshirts)+(prijs_vest*gekochte_vesten)
print(f"u kocht: \n \t Broeken: {gekochte_broeken} stuk(s) \n \t T-Shirts: {gekochte_tshirts} stuk(s) \n \t Vesten: {gekochte_vesten} stuks(s) \n Totaal: {te_betalen}")