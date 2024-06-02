a, b, c = int(input()), int(input()), int(input())
max = max(a, b, c)
min = min(a, b, c)
med = (a + b + c) - (max + min)
print(max, med, min, sep='\n')


