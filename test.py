telefoonboek = { 'Roshan': "0640780297", "hulpdiensten": "112"}
naam = input("Wie zoekt u? ")
nummer = telefoonboek.get(naam, "werd niet gevonden")
print(f"Het nummer van {naam}: {nummer}")
zoeknummer = input("Bij welk nummer zoekt u een naam?")
if zoeknummer not in telefoonboek.values():
    print("Dit nummer is onbekend!")
else:
    for naam, nummer in telefoonboek.items():
        if nummer == zoeknummer:
            print(f"Dit nummer is van {naam}")
