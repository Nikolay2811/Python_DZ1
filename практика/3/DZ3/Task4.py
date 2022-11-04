#Задайте число N. Составьте список чисел Фибоначчи, N - количество чисел в списке

a = 1
b = 1
print ('Введите число N =>')
n = int(input())
if (n == 1) :
    print(1)
elif (n == 2):
    print(1, 1)
else:
    print(a, b, end = '')
    for i in range(2, n):
     a, b = b, a + b
     print(b, end ='')