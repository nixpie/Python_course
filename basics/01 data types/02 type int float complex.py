numInt = 1000 # liczba całkowita
print(numInt)
print(type(numInt)) # <class 'int'>

numFloat = 3.14 # liczba rzeczywista
print(numFloat)
print(type(numFloat)) # <class 'float'>

numComplex = 5 + 2j
print(numComplex)
print(type(numComplex)) # <class 'complex'>

str = "Hello!"
print(str)
print( type(str) ) # <class 'str'>

print( str[0] ) # wybranie pojedynczego znaku: H
print( str[1:4] ) # ell - wybranie znaków od do
print( str * 3 ) # Hello!Hello!Hello! Powtórzenie łańcucha 3 razy
print( str + " Everyone!" ) # Hello! Everyone! - Łączenie łańczuchów dzięki konkatencji +
print("Szkolenie Python'a.") # w cudzysłowie mozna uzywac apostrofy lib odwrotnie

str = """ Pewien tekst
Kontynuacja tekstu w nowej linii,
i jeszcze jedna """
print(str)

text = ''' Następny tekst
w apostrofach '''
print(text)

str = "Pierwsza linia\nDruga linia \t oraz tabulacja \n trzecia linia"
print(str)

text = "Uzycie cudzysłowu w łańcuchu znaków jest \"mozliwe\" stosując ukośnik "
print(text)