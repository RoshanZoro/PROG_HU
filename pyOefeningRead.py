import time
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

for i in range(1,101):
    print(f"{i:3} {i:08b} {i:c}")

inp1 = int(input("Geef het eerste getal op: "))
inp2 = int(input("Geef het tweede getal op: "))
time.sleep(0.5)
for i in range(inp1, inp2):
    print(f"{i:3} {i:08b} {i:c}")


