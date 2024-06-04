n, a = int(input()), 0

while n > 9:
    a = n % 10
    n = n // 10

print(a)