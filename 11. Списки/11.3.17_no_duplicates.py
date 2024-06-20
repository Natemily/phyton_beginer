n, a = int(input()), []
for i in range(n):
    b = input()
    if b not in a:
        a.append(b)
print(*a, sep="\n")