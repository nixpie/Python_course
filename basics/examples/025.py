#if - instrukcja if a typ boolean, sktócony zapis porównania§

from socketserver import DatagramRequestHandler


data = True
if data == True:
    print("data jest True")

if data is True: # test, czy data oraz True wskazują na ten sam obiekt, b. wolne
    print("data is True")

if data: # preferowany sposób, który sprawdz,a czy data jest true
    print("data jest True")

# if - instrukcja i

data = False

if data != True: # jeśli data nie jest równe True, działa, ale nie rekomendowane
    print("data jest False")

if data is not True:    #podobnie działa ale b. wolne i nie rekomendowane
    print("data is False")

if not data:    # preferowany sposób, który sprawdze, czy data jest False
    print("data jest False")

# instrukcja wymaga wartości True, zeby zadziałała

