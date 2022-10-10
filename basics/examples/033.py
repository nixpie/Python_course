# Parametr - zmienna wewnątrz nawiasów okrągłych w definicji funkcji
def sum(a, b):
    return a + b

# Argument - wartość przesyłana do funkcji
sum1 = sum(10, 5) # da 15


print(sum1)

f = 3.2 # niemutowalne
addr1 = id(f)

f = f + 2.5
addr2 = id(f)

print(addr1)
print(addr2)
print(addr1 == addr2)

listData = ['a', 'b']   # mutowalne
addr1 = id(listData)

listData += ['c', 'd']
addr2 = id(listData)

print(addr1)
print(addr2)
print(addr1 == addr2)   # True!

# niemutowalne
def addToStr( string ):
    string += "!"
    print( "addToStr() string jako:" + string)

string = "Hello"

addToStr(string)
addToStr(string)
addToStr(string)

print("oryginalny: " + string)

# Lista mutowalna
def addToList( someList ):
    someList.append(4)

listData = [2]

addToList(listData)
addToList(listData)
addToList(listData)

print("ostateczna lista: " + str(listData) )

def addToList ( someList ):
    print("someList przed zmianą: " + str(someList) )
    someList = [30,40, 50]
    print("someList po zmianie: " + str(someList))

listData = [2]

#   przypisanie nowej listy w funkcji
#   nie zmienia listData!
addToList(listData)

print("ostateczna lista: " + str(listData) )