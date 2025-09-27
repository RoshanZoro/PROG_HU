def aantalKluizen():
    bestand = open('kluizen.txt')
    regels = bestand.readlines()
    bezetKluizen = len(regels)
    vrijeKluizen = 12 - bezetKluizen
    bestand.close()
    return vrijeKluizen
print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
keuze = int(input("Uw keuze? "))
resultaat = aantalKluizen()
if keuze == 1:
    print(f"Er zijn nog {resultaat} aantal kluizen vrij.")
