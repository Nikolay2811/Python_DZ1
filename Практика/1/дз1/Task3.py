#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3
print('Введите кординаты точки, X ≠ 0 и Y ≠ 0')
x=int(input('Ведите x => '))
y=int(input('Ведите y => '))
if (x == 0 or y == 0):
    print("Введены не верные кординаты, X ≠ 0 и Y ≠ 0")
elif ( x > 0 and y > 0):
    print('Точка расположена в первой четверти')
elif ( x < 0 and y > 0):
    print('Точка расположена во второй четверти')
elif ( x < 0 and y < 0):
    print('Точка расположена в третьей четверти')
elif ( x > 0 and y < 0):
    print('Точка расположена в четвертой четверти') 

