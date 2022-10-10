# Nazwane argumenty w funkcji

def showData(string, number):
    print(string + str(number))

showData(string = "Liczba: ", number =10)   # Liczba 10
showData(number = 10, string = "Liczba: ")  # Liczba 10

# mozna dzieki temu zmieniac kolejnosc

def printUser(name, country = "unknown", email = "default@example.com"):
    print( "User: " + name + " from country: " + country
    + " and email: " + email )

printUser(country = "UK", name = "Ania")

