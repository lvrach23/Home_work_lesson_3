#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
lenght = int(input("введите длину списка: "))
list = []
list2 = []
answer = 0
for i in range(lenght):
    list.append(int(input("Введите число: ")))
for i in range(len(list)):
    if i % 2 !=0:
        list2.append(list[i])
for i in list2:
    answer+=i
print("На нечетных позициях элементы", *list2, "ответ: ", answer)

