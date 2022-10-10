# Definiowanie funkcji - return

def printList(listData) :
    if len(listData) <= 3:
        # funkcja kończy działania
        # jeśli lista ma mniej niz
        # 3 elementy
        return
    print(listData)
    # return na końcu jest opcjonalne
    # jeśli nie zwracana jest
    # konkretna wartość
    return

printList(["a", "b", "c"])
printList(["a", "b", "c", "d", "e"])