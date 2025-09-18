
# Maak dit bestand in je project, en copy-paste daarin bovenstaande informatie.
# Schrijf een Python functie pretty_print()waarmee je het bestand opent, één string maakt zoals in het voorbeeld hieronder,
# waarbij de informatie per kaart in een nette tekst wordt weergegeven. Splits hiervoor elke regel op de komma.
# Return de uiteindelijke string aan het einde van de functie.
# Vergeet niet het bestand te sluiten!
#
# Returnwaarde van de gevraagde functie:
#
# Jan Jansen heeft kaartnummer: 325255
# Erik Materus heeft kaartnummer: 334343
# Ali Ahson heeft kaartnummer: 235434
# Eva Versteeg heeft kaartnummer: 645345
# Jan de Wilde heeft kaartnummer: 534545
# Henk de Vrie heeft kaartnummer: 345355

def prettyPrint():
    bestand = open("oefening_5_2_kaartnummers.txt")

    lijst = bestand.split(",")
