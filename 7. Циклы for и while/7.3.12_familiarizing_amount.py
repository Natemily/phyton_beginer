tl, n = 0, int(input())
for i in range(1, n+1):
    if i % 2 == 0:
        i *= -1
        tl += i
    else:
        tl += i
print(tl)