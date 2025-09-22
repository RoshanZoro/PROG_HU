
def analyse():

    lijst = "1-2-5-4-2-3-6-8-9"
    data = [int(x) for x in lijst.split("-")]
    grootste = max(data)
    kleinste = min(data)
    data.sort()
    elkaar = sum(data)
    aantal = len(data)
    gemiddeld = elkaar / len(data)
    resultaat = (data, grootste, kleinste, elkaar, gemiddeld, aantal)
    return resultaat

print(f"Gesorteerde list van ints: {analyse()[0]}")
print(f"Grootste getal: {analyse()[1]} en kleinste getal: {analyse()[2]}")
print(f"Aantal getallen: {analyse()[5]} en de Som van de getallen: {analyse()[3]}")
print(f"Gemiddelde: {analyse()[4]}")
