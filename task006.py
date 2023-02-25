from math import sqrt
s, p = map( int, input('Задайте сумму s и произведение p чисел, через запятую: ').split(',') )
z = sqrt( (s/2)**2 - p )
print( int( s/2 - z ), int( s/2 + z ) )


