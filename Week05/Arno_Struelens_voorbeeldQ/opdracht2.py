# Vul onderstaande functies aan. Vergeet de parameters niet aan te vullen (zie opgave)!!!
# Test onderaan alle functies voldoende uit

def filter_misses_postcode(par_kleinste, par_grootste, dictionary):
    res_list = []
    for (key,value) in dictionary.items():
        if value in range(par_kleinste,par_grootste+1):
            res_list.append(key)
    return res_list
            


misses_2019 = {"Marieke": 8800, "Delfien": 8500, "Mieke": 8531, "Els": 9070, "Lola":  2500,
               "Dolly": 9999, "Marianne": 9000, "Claudine": 2800, "Lies": 3080, "Jacqueline": 3720, "Jozefien": 8700}
misses_2018 = {"Tine": 3700, "Anke": 8700, "Claudia": 8530, "Marijn": 9000,
               "Sofie":  2650, "Marie": 9870, "Leen": 9000, "Conny": 2800}
kleinste_postcode = int(input("Geef de kleinste postcode: >"))
grootste_postcode = int(input("Geef de grootste postcode: >"))

# Test hier bovenstaande functies uit (zie opgave voor meer detail)
print(f"Dit zijn de gevonden missen uit 2018:\n {filter_misses_postcode(kleinste_postcode,grootste_postcode, misses_2018)}")
print(f"Dit zijn de gevonden missen uit 2019:\n {filter_misses_postcode(kleinste_postcode,grootste_postcode, misses_2019)}")
