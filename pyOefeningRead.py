bestand = open("huisgenoten.txt")
regels = bestand.readlines()
leeftijdTotaal = 0
print(f"Aantal regels: {len(regels)}")
for huisgenoot in regels:
    huisgenoot = huisgenoot.strip()
    details = huisgenoot.split(",")
    naam = details[0]
    leeftijd = int(details[1])
    leeftijdTotaal += leeftijd
    if leeftijd < 1:
        categorie = "baby"
    elif leeftijd < 18:
        categorie = "kind"
    else:
        categorie = "volwassen"
    print(f"{naam.upper()}: {categorie}")
bestand.close()



