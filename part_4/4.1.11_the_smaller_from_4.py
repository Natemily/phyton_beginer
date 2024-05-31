a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a <= b:
    if c <= d:
        if a <= c:
            print(a)
        else:
            print(c)
    else:
        if a <= d:
            print(a)
        else:
            print(d)
else:
    if c <= d:
        if c <= b:
            print(c)
        else:
            print(b)
    else:
        if d <= b:
            print(d)
        else:
            print(b)