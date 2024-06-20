nml = int(input())
l = nml % 10
m = (nml % 100) // 10
n = nml // 100
print('Сумма цифр =', l+m+n)
print('Произведение цифр =', l*m*n)