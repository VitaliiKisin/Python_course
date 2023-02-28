n = int(input('Введите число N первого множества: '))
num_list_1=[]
for i in range(n):
    # Введите элементы первого множества, каждый с новой строки:
    num = int(input("Введите элемент: "))
    num_list_1.append(num)
print(num_list_1)

m = int(input('Введите число M второго множества: '))
num_list_2 = []
for i in range(m):
    # Введите элементы второго множества: 
    num = int(input("Введите элемент: "))
    num_list_2.append(num)
print(num_list_2)

num_list3 = num_list_1 + num_list_2
print(num_list3)
for i in set(num_list3):
    if num_list3.count(i) > 1:
        print(i)

#    print(num_list3)
#    for i in num_list3:
#     if num_list3.count(i) > 1:
#       print(i)


# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#  Выдать без повторений в порядке возрастания все те числа, которые встречаются в
#  обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
#  m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.