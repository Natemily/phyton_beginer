from math import tan, pi, radians
n, a = int(input()), float(input())
rad = radians(n)
print((n*a**2)/(4*tan(pi/n)))