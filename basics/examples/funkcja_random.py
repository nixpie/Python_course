import random

# losowy float od 0 i mniejszy od 1 np. 0.92
print( random.random() )

# losowy  element z listy, krotki lub str
print( random.choice([4,3,8]) )                     # np. 3
print( random.choice(("Ola", "Ania", "Adam")) )     # np. Ola

# losowy element z zakresu: start, stop, step
print( random.randrange(0,25,5) )                   # np. 20

# ustawia losowo elementy listy
listData = [0,1,2,3,4]
random.shuffle(listData)
print( listData )                                   # np. [2, 4, 0, 3, 1]

# losowy float większy od x i mniejszy od y
print( random. uniform(2.3 , 10.78) )               # np. 7.8671

# Dodatkowo python oferuje wiele funkcji trygonometrycznych jak acos(), asin(), atan(), cos() itd.