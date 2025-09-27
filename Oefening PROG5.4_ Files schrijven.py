# Bij een marathonwedstrijd worden bij een controlepost alle voorbijkomende hardlopers genoteerd.
# De gegevens van elke hardloper worden in het bestand oefening_5_4_hardlopers.txt opgeslagen.
# Schrijf een programma waarmee een tekstbestand wordt aangemaakt (als het bestand nog niet bestaat) of aangevuld
# (gebruik de append-mode) met de gegevens van één hardloper (inlezen van toetsenbord).
#
# Let op: je zult je programma in deze opdracht steeds opnieuw moeten uitvoeren voor elke nieuwe hardloper.
# Om dit te voorkomen zou je een while-loop kunnen gebruiken, maar die behandelen we pas volgende les.
# Je kunt er natuurlijk voor kiezen om daar alvast naar te kijken (niet verplicht).

from datetime import datetime


def marathon():
    gegevens = input("Naam hardloper: ")
    nu = datetime.now()
    with open("oefening_5_4_hardlopers.txt", "a") as bestand:
        bestand.write(f"{nu.strftime("%a %d %b %Y, %H:%M:%S")}, {gegevens}\n")


marathon()