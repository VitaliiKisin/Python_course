n = int(input('Задайте количество монет n = '))
count_one = 0
count_tow = 0
for i in range(n):
    x = int(input())
    if x == 0:
        count_one += 1
    else:
        count_tow += 1
if count_one > count_tow:
    print(count_tow)
else:
    print(count_one)







# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть