# pętla for

listData = [1,2,3,4]                    # iteracja listy
for v in listData:
    print (v)

tupleData = ("one", "two", "three")     # iteracja krotki
for v in tupleData:
    print(v)

setData = {3,2,1}                       # iteracja zbioru
for v in setData:
    print(v)

strData = "Hello"                       # iteracja Stringa
for v in strData:
    print(v)

# iteracja słownika
dictionaryData = { "Ola" : "ola@example.com", "Ania" : "ania@exemple.com" }
for v in dictionaryData:
    print(v)                            #wyświetlenie kluczy słownika

# iteracja słownika, pokazanie wartości
dictionaryData = { "Ola" : "ola@example.com", "Ania" : "ania@exemple.com" }

for v in dictionaryData:
    print( dictionaryData[v] )          # wyświetlanie wartości słownika

# iteracja słownika
dictionaryData = { "Ola" : "ola@example.com", "Ania" : "ania@exemple.com" }

for key, value in dictionaryData.items():
    print( key, " : ", value )          # klucz i wartość

for key in dictionaryData.keys():
    print( key )          # wyświetlanie klucza

for value in dictionaryData.values():
    print( value )          # wyświetlanie wartości

for value in dictionaryData.values():
    print( value )          # wyświetlenie wartości
else:
    print( "for loop ended" )

