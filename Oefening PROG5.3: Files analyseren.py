# Schrijf een programma waarmee je het bestand 'oefening_5_2_kaartnummers.txt',
# opnieuw opent en het aantal regels, het grootste kaartnummer en de regel waarop dit grootste
# kaartnummer in het bestand staat, bepaalt. Print deze gegevens vervolgens uit:
#
# Uitvoer:
# Deze file telt 6 regels
# Het grootste kaartnummer is: 645345 en dat staat op regel 4
data = open("oefening_5_2_kaartnummers.txt")
nummers = data.readlines()
lijst = []
def analyse():
    for lijn in nummers:
        lijst.append(int(lijn))

print(lijst)
