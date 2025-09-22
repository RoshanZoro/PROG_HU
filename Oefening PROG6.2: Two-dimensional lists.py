studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
    antw = []
    for cijfers in studentencijfers:
        gem = sum(cijfers) / len(cijfers)
        antw.append(gem)
    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    alleCijfers = []
    for student in studentencijfers:
        for cijfer in student:
            alleCijfers.append(cijfer)
    antw = [sum(alleCijfers) / len(alleCijfers)]
    return antw

print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))
