# naam: Stroobant Bert
# groep:1MCT4
# pas de code verder aan
mijn_scores1 = [12, 10, 14, 12, 16, 20]
gewicht_modules1 = [6, 3, 6, 6, 6, 9]

mijn_scores2 = [18, 15, 14, 18, 17, 18]
gewicht_modules2 = [6, 3, 6, 6, 6, 9]

mijn_scores3 = [15, 14, 18, 7]
gewicht_modules3 = [6, 6, 3, 9]

def bereken_graad_diploma(lst_scores, lst_gewicht_modules):
    totaal_score = 0
    totaal_gewicht = 0
    for score, gewicht in zip(lst_scores, lst_gewicht_modules):     #lst_scores en lst_gewichten lijn per lijn inlezen
        totaal_gewicht += gewicht       #totaal gewicht berekenen voor breuk
        totaal_score += score*gewicht   #bovenste helft breuk berekenen
    totaal_score /= totaal_gewicht
    if totaal_score >= 16.5:            #graad berekenen op basis van totaal_score
        graad = "geslaagd met de grootste onderscheiding"
    elif totaal_score < 16.5 and totaal_score >= 15:
        graad = "geslaagd met grote onderscheiding"
    elif totaal_score < 15 and totaal_score >= 13.5:
        graad = "Geslaagd met onderscheiding"
    elif totaal_score < 13.5 and totaal_score >= 10:
        graad = "Geslaagd op voldoende wijze "
    else:
        graad = "U bent niet geslaagd"
    return graad                        #graad in tekst als return waarde 

graad1 = bereken_graad_diploma(mijn_scores1, gewicht_modules1)  #graad berekenen met gegevens van persoon 1
print(f"Graad op diploma van student 1: {graad1}")              #return waarde wordt geprint

graad2 = bereken_graad_diploma(mijn_scores2, gewicht_modules2)  #graad berkenen met gegevens van persoon 2
print(f"Graad op diploma van student 2: {graad2}")

graad3 = bereken_graad_diploma(mijn_scores3, gewicht_modules3)  #graad berekenen met gegevens van persoon 3
print(f"Graad op diploma van student 3: {graad3}")
