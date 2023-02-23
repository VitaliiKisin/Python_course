n = str(input("Введите номер билета : ")) 

s1 = int(n[0]) + int(n[1]) + int(n[2])
s2 = int(n[3]) + int(n[4]) + int(n[5])

if s1 == s2:
  print("Счастье в ваших в руках")
else:
  print("Не фортит")
##print((lambda x: ('Несчастливый', 'Cчастливый')[sum(x[:3]) == sum(x[3:])])((*map(int, input('N=')),)))


