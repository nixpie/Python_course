set = {0, 4, 8, 12, 16}
set.add(20)

frozen = frozenset(set)
print(frozen)               #frozenset({0, 16, 4, 20, 8, 12})

frozen.add(24)              # błąd! nie ma add()

#iterowanie elementów w zestawie
for value in frozen:
    print(value)