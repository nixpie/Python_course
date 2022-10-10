set = {0, 4, 8, 12, 16}
set.add(20)
print(set)  # {0, 16, 4, 20, 8, 12}

set.add(20) # wartość juz jest, więc pominięta
set.add(24)
set.discard(8)  # skasowanie wartości 8
print(set)  # {0, 16, 4, 20, 24, 12}

# iterowanie elementów w zestawie
for value in set:
    print(value)