leeftijd = int(input("Geef je leeftijd: "))
nederlandsPaspoort = input("Nederlands paspoort: ")
if leeftijd >= 18 and nederlandsPaspoort.lower() == "ja":
    print("Gefeliciteerd, je mag stemmen!")
else:
    print("Sorry, je mag niet stemmen.")