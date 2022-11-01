#Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно
print('Введите N для промежутка [1, N]')
n =int(input())
ran = range (1, n+1)
mass1 = list(ran)
print(mass1)
i = 1
res = 0
while i < n:
    res = res + mass1[i]
    i+=2
print(f'Сумма четных чисел в помежутке [1, {n}] равна {res}')