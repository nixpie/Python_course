# Scope zasięg zmiennych = zmienne lokalne

number = 20

def printNumber():
    print(number)       # dostęp do zmiennej globalnej, poniewaz nie ma takiej funkcji
    string = "test"     # zadeklarowana zmienna lokalna
    print(string)

printNumber()
# id(string)              # brak dostępu do string, bo jest zmienną lokalną

number = 12     # zmienna globalna

print(number)   # 12

if number > 0:
    print(number)   # instrukcja if ma dostęp do zmiennej globalnej

def printNum():
    print(number)   # funkcja ma dostęp do globalnej zmiennej

number = 20

def printNumber():
    number = 6                  # deklaracja zmiennej lokalnej o tej samej nazwie przesłania globalną
    print("number: ", number)   # odwołanie po number odnosi się do lokalnej zmiennej

printNumber()

string = "Hello"

def printData(string):
    print(2, string)    # zmienna jako argument przesłania globalną o tej samej nazwie

print(1, string)        # 1 Hello
printData("Test")

string = "Hello"

def showInfo():
    print(3, string)    # Uwaga, odwołanie do zmiennej globalnej!: 3, Hello

def printData():
    string = "Test"     # zmienna lokalna przesłania globalną
    print(2, string)    # 2, Test
    showInfo()          # wywołanie funkcji showInfo()

print(1, string)        # Hello
printData()

firstNum = 9

def test():
    firstNum = 1
    print("test() firstNum:", firstNum)
    def bar():
        print("bar() fisrtNum:", firstNum)
    bar()
    print("end test()")

print("global firstNum:", firstNum)
test()

# global - odwoływanie się do globelnej zmiennej wewnątrz funkcji

number = 20

def printNumber():
    # nie modyfikujemy globalnej tylko
    # tworzymy lokalną zmienną!
    number = 33 # nie zmieni zmiennej globalnej
    print("doNumber(): ", number)

printNumber()
print("global number", number)

# uzycie global

number = 20

def printNumber():
    global number   # number wskazuje
                    # na globalną
    number = 33     # modyfikacja
                    # globalnej!
    print("doNumber(): ", number)

printNumber()
print("global number", number)

# instrukcja if nie definiuje zasięgu tak samo jak pętle i try / except

string = "Hello"

if 1 == 1:
    print(1, string)            # Hello
    if 2 == 2:
        string = "Test"         # zmiana globalnego string
        print(2, string)        # 2, Test
        if( 3 == 3):
            print(3, string)    # 3, Test

print(4, string)                # 4 Test


string = "Hello"

def testFunc():
    string = "Local Hi"
    if 1 == 1:
        print(1, string)            # 1 Local Hi
        if 2 == 2:
            string = "Test"         # zmiana string wewnątrz funkcji!
            print(2, string)        # 2 Test
            if( 3 == 3):
                print(3, string)    # 3 Test
    print(4, string)                # 4 Test

testFunc()
print(5, string)                # 5 Hello


if 1 == 1:
    data = "some data"      # zdefiniowanie zmiennej, tutaj globalnej

print(data)                 # some data

if 2 == 1:
    info = 10

#print(info)                 # błąd name 'info' is not defined