n, s = int(input()), 0
while n > 0:
    while n > 9:
        s += n % 10
        n = n // 10
    s += n
    if s < 10:
        n = 0
    else:
        n = s
        s = 0
   
print(s)