def aanbieding_1(smaak, prijs, korting):
    korting = prijs * (1 - korting)

    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro"
    return uitvoer

