def geef_provincie (par_postcode):
    provincie = ""
    if par_postcode  in range(1500,1999 +1):
        provincie = "Vlaams-Brabant"
        
    elif par_postcode in range(2000,2999 +1):
        provincie = "Antwerpen"

    elif par_postcode  in range(3000,3499+1):
        provincie = "Vlaams-Brabant"

    elif par_postcode in range(3500,3999 +1):
        provincie = "Limburg"

    elif par_postcode in range(8000,8999 +1):
        provincie = "West-Vlaanderen"

    elif par_postcode in range(9000,9999 +1):
        provincie = "Oost-Vlaanderen"
    else:
        print("error")
    return provincie
    
postcode = int(input(f"Geef de postcode op: > "))
print(f"De provincie van de postcode {postcode} is: {geef_provincie(postcode)}.") 