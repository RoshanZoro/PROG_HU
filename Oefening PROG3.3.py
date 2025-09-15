maandNummer = int(input("Geef een maandnummer: "))
lente = [3, 4, 5]
zomer = [6, 7, 8]
herfst = [9, 10, 11]
winter = [12, 1, 2]
if maandNummer > 12:
    print("Dit is geen geldige maandnummer!")
elif maandNummer < 1:
    print("Dit is geen geldige maandnummer!")
if maandNummer in lente:
    print("Het is lente.")
elif maandNummer in zomer:
    print("Het is zomer.")
elif maandNummer in herfst:
    print("Het is herfst.")
elif maandNummer in winter:
    print("Het is winter")