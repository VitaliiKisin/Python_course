n = int(input("Задайте количество элементов N "))
a = map(int, input("Напишите N любых чисел, через пробел ").split(" "))
x = int(input("Введите необходимое число "))

closest = x + 2001
mindiff = 2001

for el in a:
	if abs(x - el) <= mindiff:
		if abs(x - el) == mindiff:
			closest = min(closest, el)
		else:
			closest = el			
			mindiff = abs(x - el)

print(closest)

