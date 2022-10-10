#   funkcje bezargumentowe

def printSomething():
    print("Some information!")

printSomething()
printSomething()
printSomething()


#   funkcje z argumentami - trzeba przekazywać dane w odpowiedniej kolejności

def showData(string, number):
    print(string + str(number))

# Łańcuch "Liczba: " będzie dostępny w funkcji jako zmienna string
# Liczba 10 będzie dostępna w funkcji jako zmienna number
showData("Liczba: ", 10)

# gdy przekazemy dane w złej kolejności
# to zwykle skończy się to błędem
# showData(10, "Liczba: " )    # błąd!

# Domyślne wartości argumentów funkcji
def printUser(name, country = "unknown", email = "default@example.com"):
    print( "User: " + name + " from country: " + country
    + " and email: " + email )

printUser("Adam", "Poland", "adam@example.com")     # nadpisanie domyślne wartości

printUser("Ola")    # wartości domyślne będą uzyte w funkcji