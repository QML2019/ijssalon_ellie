prijzen = {
    "aardbei" : "3",
    "vanille" : "4",
    "chocolade" : "5"
}

aanbieding = (3*0.8)

reclame_tekst = (f"Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts € {aanbieding}")
reclame_tekst2 = (reclame_tekst[:63])
reclame_tekst3 = (f"VANDAAG IN DE AANBIEDING: AARDBEI-IJS, 1 LITER - SLECHTS € {aanbieding}")
reclame_tekst4 = ["VANDAAG", "IN", "DE", "AANBIEDING", "AARDBEI-IJS", "1 LITER", "SLECHTS", "2.40"]

for el in reclame_tekst4:
    print(el.lower())










