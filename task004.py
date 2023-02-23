n = int(input("Введите n ")) 
m = int(input("Введите m "))
k = int(input("Введите k "))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('Ломайте смело шоколад')
else:
    print('Очень сомнительный разлом шоколада')

#n, m, k = int(input()), int(input()), int(input())
#print(['NO', 'YES'][not (k % n and k % m)])



