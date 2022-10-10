
listData = [1,2,3,4,5,6]

tupleData = tuple(listData)
print(tupleData)

otherList = list( ("Ola", 23, 254) )
print(otherList)

setData = (set(otherList))
print( type(setData) )
print(setData)

frozenSetData = frozenset(tupleData)
print( type(frozenSetData) )
print(frozenSetData)

tupleData = ( ("Ola", 1234), ("Adam", 2564) )

dictData = dict(tupleData)
print(dictData)
print(dictData["Ola"])

