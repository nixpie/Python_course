import math

# wartość bezwzględna
print( abs(5) )     # 5
print( abs(-5) )    # 5

# zaokrąglenie do najmniejszej liczby
# całkowitej nie mniej niz podana wartość
print( math.ceil(6.78) )    # 7
print( math.ceil(20.12) )   # 21
print( math.ceil(-3.23) )   # -3

# zaokrąglenie do największej liczby
# całkowitej nie większej niz podana wartość
print( math.floor(6.78) )       # 6
print( math.floor(20.12) )      # 20
print( math.floor(-3.23) )      # -4

# max zwróci największą wartość z przekazanych
print( max(12, 3, 78, 32, 11) )     # 78
print( max(9, 67, 43, -2) )         # 67

# min zwróci najmniejszą wartość z przekazanych
print( min(12, 3, 78, 32, 11) )     # 3
print( min( [9, 67, 43, -2] ) )     # -2

print( pow(2, 3) )              # to samo jak x**y = 8
print( math.sqrt(16) )          # pierwiastek 4.0
print( round(23.12345, 3) )     # zaokrąglenie do 3. miejsca po przecinku: 23.123