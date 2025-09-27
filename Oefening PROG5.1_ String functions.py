# Schrijf functie gemiddelde(), die de gebruiker vraagt om een willekeurige zin in te voeren.
# De functie geeft vervolgens de gemiddelde lengte van de woorden in de zin als returnwaarde terug.
# Test je code door de methode aan te roepen en het resultaat te printen.



def gemiddelde():
    zin = input("Voer een willekeurige zin in: ")
    woordenLijst = zin.split()
    totaalLijst = 0
    for woord in woordenLijst:
        totaalLijst += len(woord)
    resultaat = totaalLijst / len(woordenLijst)
    return resultaat

print (gemiddelde())
