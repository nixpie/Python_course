
print(bool())               #False

# falsy values, czyli wartości, które dają False przy konwersji na boolean
print( bool(False) )        #False
print( bool(0) )            #False
print( bool(0.0) )          #False
print( bool( () ) )         #False
print( bool( [] ) )         #False
print( bool( {} ) )         #False
print( bool( '' ) )         #False
print( bool( None ) )       #False

print( bool(True) )         #True
print( bool(10) )           #True
print( bool(-10) )          #True
print( bool(-12.234) )      #True
print( bool( (1,2,3,4) ) )  #True
print( bool( [0] ) )        #True
print( bool( {0} ) )        #True
print( bool( "z" ) )        #True


data = None

print(type(data))           #<class 'NoneType'>

if data is True:
    print("Data is true")
elif data is False:
    print("Data is False")
else:
    print("None is None")