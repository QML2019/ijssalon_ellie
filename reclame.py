def mijn_functie_2(a,b):
    return (a + b), (a - b), (a * b), (a / b)

def aanbieding_1(smaak, prijs, korting):
    korting = prijs * (1 - korting)

    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro"
    return uitvoer

print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for nr in inkomsten:
        totaal += nr
    btw_bedrag = totaal * btw
    uitvoer = f"Het totaal van alle inkomsten deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
    return uitvoer

print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09))

def laag_en_hoog(mijn_lijst):
    uitvoer = []
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    uitvoer.append(hoogste)
    uitvoer.append(laagste)
    return uitvoer
    
laag_hoog = laag_en_hoog([220, 430, 125, 160, 205, 90, 345])
print(laag_hoog)

def gemiddelde(mijn_lijst):
    aantal = len(mijn_lijst)
    totaal = 0
    for element in mijn_lijst:
        totaal += element
    bedrag = (totaal/aantal)
    uitvoer =  f"De gemiddelde inkomsten deze week zijn {bedrag} euro"
    return uitvoer

Uitkomst = gemiddelde([220, 430, 125, 160, 205, 90, 345])
print(Uitkomst)

def meervoudig(invoer_lijst):
    tijdelijk = laag_en_hoog(invoer_lijst)
    uitvoer = [tijdelijk[0], tijdelijk [1]]
    return uitvoer

Uitkomst = meervoudig ([10,5,3,2,1,2,9])
print(Uitkomst)

def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer







