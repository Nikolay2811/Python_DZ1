#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. Примечание:
#Используйте знания об Алгебра Логике, вы должны перебрать все возможные комбинации значений X, Y, Z (принимают значения 0 или 1)
print('Проверим истиность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')


for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
         left=not(x or y or z)
         right=not x and not y and not z
         res = right == left
         print(f'выражения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z принимает значение при x ={x}, y ={y}, z ={z} =>', res)
         
            
