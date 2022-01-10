# Vul onderstaande functies aan. Vergeet de parameters niet aan te vullen (zie opgave)!!!
# Test onderaan alle functies voldoende uit
def geef_aantallen_per_provincie(dict_missen):
    new_dict = {}
    for key, value in dict_missen.items():
        if value  in range(1500,1999 +1):
            new_dict["Vlaams_brabant"] = new_dict.get("Vlaams-Brabant",0)
        
        elif value in range(2000,2999 +1):
            new_dict["Antwerpen"] = new_dict.get("Antwerpen",0)
        
        elif value  in range(3000,3499+1):
            new_dict["Vlaams_brabant"] = new_dict.get("Vlaams-Brabant",0)

        elif value in range(3500,3999 +1):
            new_dict["Limburg"] = new_dict.get("Limburg",0)

        elif value in range(8000,8999 +1):
            new_dict["West-Vlaanderen"] = new_dict.get("West-Vlaanderen",0)

        elif value in range(9000,9999 +1):
            new_dict["Oost-vlaanderen"] = new_dict.get("Oost-Vlaanderen",0) 

    for key, value in dict_missen.items():
        if value  in range(1500,1999 +1):
            new_dict["Vlaams_brabant"] +=1
        
        elif value in range(2000,2999 +1):
            new_dict["Antwerpen"] +=1
        
        elif value  in range(3000,3499+1):
            new_dict["Vlaams_brabant"] +=1

        elif value in range(3500,3999 +1):
            new_dict["Limburg"] +=1

        elif value in range(8000,8999 +1):
            new_dict["West-Vlaanderen"] +=1

        elif value in range(9000,9999 +1):
            new_dict["Oost-vlaanderen"] +=1 
    return new_dict

misses_2019 = {"Marieke": 8800, "Delfien": 8500, "Mieke": 8531, "Els": 9070, "Lola":  2500,
               "Dolly": 9999, "Marianne": 9000, "Claudine": 2800, "Lies": 3080, "Jacqueline": 3720, "Jozefien": 8700}
misses_2018 = {"Tine": 3700, "Anke": 8700, "Claudia": 8530, "Marijn": 9000,
               "Sofie":  2650, "Marie": 9870, "Leen": 9000, "Conny": 2800}



# Test hier bovenstaande functies uit (zie opgave voor meer detail)
print(f"Aantal missen per provincie uit 2018:\n{geef_aantallen_per_provincie(misses_2018)}")
print(f"Aantal missen per provincie uit 2019:\n{geef_aantallen_per_provincie(misses_2019)}")
