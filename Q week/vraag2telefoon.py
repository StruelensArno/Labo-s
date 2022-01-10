# naam: Stroobant Bert
# groep: 1MCT4
dict_telefoonboek = {"Tom": "056908652", "Nathan": "053907851", "Stijn": "010561247",
                     "Dieter": "056231457", "Marie": "019875412", "Christophe": "064123258", "Gilles": "056985201"}
dict_antwoordapparaat = {"Nathan": "Hallo ik bel even om...", "Dieter": "Hey, het is om te zeggen dat...",
                         "Gilles": "Wow, moet je nu eens horen...", "Stijn": "Oei, verkeerd verbonden."}


# gebruik de functie zoek_personen_uit_zone
def zoek_personen_uit_zone (dict_telefoon, zonenummer): 
    lst_namen = []
    print(f"Deze personen komen uit de zone {zonenummer}: ")
    for key, value in dict_telefoonboek.items():
        nummer = value[0:3]
        if zonenummer == nummer: 
            lst_namen.append(key) #naam toevoegen aan lijst met namen
            print(f"- {key}")
    return lst_namen

# gebruik zoek_gesprekken_personen en print_gesprekken_af
def zoek_gesprekken_personen(dict_opgenomen, lst_personen):
    dict_opgenomen_gesprekken = {}
    count = 0       #totaal aantal opgenomen besprekken worden hier geteld
    print("\nFunctie2:\nOpzoeken gesprekken van lijst personen...")
    for key, value in dict_opgenomen.items():
        if key in lst_personen:
            dict_opgenomen_gesprekken[key]=value    #dict_opgenomen_gesprekken invullen met key en value uit dict_opgenomen met de key die ook aanwezig is in lst_personen
            count += 1
    print(f"Er werden {count} gesprekken opgenomen\n")
    return dict_opgenomen_gesprekken    #dict met personen en opgenomen gesprekken terug geven

def print_gesprekken(dict_gesprekken):
    print("functie3:\nopgezochte gesprekken afspelen:\nWelkom bij je antwoordapparaat.\nDit zijn de geselecteerde gesprekken:")
    for key, value in dict_gesprekken.items():
        print(f"{key}\t:\t{value}")     #dict lijn per lijn afprinten

print("Functie1:")
nummer = input("Geef een zonenummer op > ")

lst_personen = zoek_personen_uit_zone(dict_telefoonboek, nummer)

gesprekken_personen = zoek_gesprekken_personen(dict_antwoordapparaat, lst_personen)

print_gesprekken(gesprekken_personen)

