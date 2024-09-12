n, a, b = int(input()), [], []
for i in range(n):
    a.append(int(input()))
for i in range(len(a)):
    c = a[i]**2+a[i]*2+1
    b.append(c)
print(*a, sep="\n")
print()
print(*b, sep="\n")