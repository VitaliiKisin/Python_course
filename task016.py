import random
arr = []
for i in range(20):
	x = int(random.random()*10)  
	arr.append(x)
	print("%3d" % x, end='')
	if (i+1) % 10 == 0:	print()
 
minimum = int(input('min: '))
maximum = int(input('max: '))
 
index = []
i = 0
for i in range(len(arr)):
	if minimum <= arr[i] <= maximum:
		index.append(i)
		
print("Количество: ", len(index))
print("Индексы: ", index)
b = [] # Удаленные с конца списка числа заданного диапазона 
for i in index[::-1]:
	b.append(arr.pop(i))

print(b)
print("Обновлённый список", arr)

# Определить индексы элементов списка, значения которых принадлежат заданному
#  диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
#  (и после того, как элемент с подходящим значением добавлен в новый список –
#  удалять его из исходного списка)