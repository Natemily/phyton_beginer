from math import sqrt
a, b, c = float(input()), float(input()), float(input())
d = b**2 - 4*a*c
if d > 0:
    x1 = (-b - sqrt(d)) / (2 * a)
    x2 = (-b + sqrt(d)) / (2 * a)
    max = max(x1, x2)
    min = min(x1, x2)
    print(min, max, sep='\n')
elif d == 0:
    x1 = -b / (2 * a)
    print(x1)
else:
    print("Нет корней")