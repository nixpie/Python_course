# instrukcja warunkowa if

number = 10

if number > 6:
    print("number większe od 6")
    print("tez się wyświetli, jesli numer > 6")

if number == 2:
    print("number równe 2")


# if bloki kodu oraz wcięcia

num = 12
if num > 5:
    print( str(num) + "Większe od 5" )
    # instrukcje if mona zagniezdzać
    if num >= 10:
        print( str(num) + " większe tez od 10" )
        if num > 20:
            print( str(num) + "większe tez od 20")
    print("Ostatnie wzięcie instrukcji if")

print("Informacja niezalezna od bloku kodu if")

# instrukcja elif

num = 7
if num == 7:
    print("num jest 7")
elif num == 10:
    print("nume jest 10")

num = 10
if num == 7:
    print("num jest 7")
elif num == 10:
    print("num jest 10")

num = 20

if num ==7:
    print("num jest 7")
elif num == 10:
    print("num jest 10")
elif num == 12:
    print("num jest 12")
elif num == 14:
    print("num jest 14")
elif num >= 15:
    print("num jest większe równe 15")

#else

a = 10
b = 5

if a == b:
    print("a równe b")
elif a < b:
    print("a < b")
else:
    print("a > b")

# wrto wwarto równiez wspomnie, ze mozna zapisac
# w jednej linijce kod do wykonania po if

if a > b: print ("a większe od b")