intNum = 20
print( type(intNum) )   # <class 'int'>

floatNum = float(intNum)    # konwersja int na float
print(floatNum)             # 20.0
print( type(floatNum) )     # <class 'float'>

f = float("76.789")         # 76.789
print(f)                    
print(type(f))              # <class 'float'>

#zła liczba w łańcuchu powoduje błąd
#float("1234,34")            # ValueError: could not convert string to float: '1234,34'

str1 = str(intNum)          # konwersja int na łańcuch znaków
print(str1)                 # 20
print( type(str1) )         # <class 'str'>

str2 = str( 45.456 )
print(str2)
print(type(str2))           # <class 'str'>

print("Rok ma " + str(365) + " dni.")   #Rok ma 365 dni.

#TypeError: can only concatenate str (not "int") to str
print("Rok ma " + 365 + " dni. ")