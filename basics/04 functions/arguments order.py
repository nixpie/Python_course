
def printCar(brand, / ,name = "concept", * ,year = 1960, color = "black"):
    print(brand, name, year, color)


# printCar(brand = "Ford", "Mustang", color = "blue", year = 1973)    # błąd
printCar("Ford", name = "Mustang", color = "blue", year = 1973)
# printCar("Ford", name = "Mustang", "blue", year = 1973)               # błąd

# / wszystkie argumenty PRZED sleszem muszą być w odpowiedniej kolejności i NIE MOGA być nazwane
# * wszystkie argumenty ZA gwiazdką MUSZA być nazwane

