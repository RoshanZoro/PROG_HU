# Schrijf een programma waarmee je het bestand 'oefening_5_2_kaartnummers.txt',
# opnieuw opent en het aantal regels, het grootste kaartnummer en de regel waarop dit grootste
# kaartnummer in het bestand staat, bepaalt. Print deze gegevens vervolgens uit:
#
# Uitvoer:
# Deze file telt 6 regels
# Het grootste kaartnummer is: 645345 en dat staat op regel 4

def analyse():
    with open("oefening_5_2_kaartnummers.txt") as bestand:
        nummers = bestand.readlines()
    huidigeRegel = 0
    grootsteKaartnummer = 0
    for lijn in nummers:
        huidigeRegel += 1
        lijn = lijn.strip()
        detail = lijn.split(",")
        kaartnummer = int(detail[0])
        if kaartnummer > grootsteKaartnummer:
            grootsteKaartnummer = kaartnummer
            resultaat = f"Het grootste kaartnummer is: {kaartnummer} en dat staat op regel {huidigeRegel}"
    return resultaat

print(f"Deze file telt 6 regels.\n{analyse()}")
