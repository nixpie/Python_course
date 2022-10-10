# pętla while

number = 4

while number > 0:
    print(number)
    number = number - 1

print("Kod pętli")


# pętla nieskończona

num = 0
# pętla nieskończona
while( True ):
    print("Wprowadź w konsoli liczbę do dodanie, exit aby zakończyć")
    strData = input() # odczyt danych od uytkownika
    if(strData == "exit"): break # wyjście z pętli jeśli warunek jest spełniony
    num += int(strData)
    print("Nowa wartość" + str(strData) + " jest" + str(num) )

print("Ostateczna wartość po pętli: " + str(num) )

