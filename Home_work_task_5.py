#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример: - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21

number = int(input("введите число: "))
fibonachi_clasik = [0,1]
fibonachi_nega = [1,0]
for i in range(number-1):
    fibonachi_clasik.append(fibonachi_clasik[i] + fibonachi_clasik[i+1]) 
for i in range(number-1):
    fibonachi_nega.insert(0, fibonachi_nega[1]+((-1)*(fibonachi_nega[0])))       
   
fibonachi_clasik.pop(0)
fibonachi_final= fibonachi_nega + fibonachi_clasik      

print(fibonachi_final)
