
for v in [1,2,3,4]:
    print(v * 2)

for v in ("Ania", "Ola", "Rafał"):
    print(v)

for el in {3,4,5,6, "Ola"}:
    print(el)

for v in "Hello":
    print(v)
else:
    print("pętla zakończona")

dictionaryData = { "Ania" : "ania@example.com", "Adam" : "adam@example.com" }

for key in dictionaryData:
    print(key)

for key in dictionaryData.keys():
    print(key)

for key in dictionaryData.keys():
    print( dictionaryData[key] )

for key, value in dictionaryData.items():
    print( key, " : ", value )

for v in dictionaryData.values():
    print(v)

for v in range(3): # [0,1,2]
    print(v)

for v in range(2, 5): # [2,3,4]
    print(v)

# range(start, end, step)
for v in range(2, 8, 2):    # [2,4,6]
    print(v)
