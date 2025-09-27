klinker = ["a", "e", "i", "o", "u"]
s = "Guido van Rossum heeft programmeertaal Python bedacht."
for letter in s:
    if letter in klinker:
        print(letter)