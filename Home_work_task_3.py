#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
#и минимальным значением дробной части элементов.(если получаются длинные числа после запятой, 
#это нормально и особенность данного языка программирования. ваш ответ может не совпадать с примером(может получитя 0,20))
#Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
max=0
min=1
for i in list:
    if i - (int(i)) > max: 
        max = round((i-(int(i))), 2)
    elif i - (int(i)) < min and i - (int(i)) > 0:
        min = round((i-(int(i))), 2)
print(max-min)
