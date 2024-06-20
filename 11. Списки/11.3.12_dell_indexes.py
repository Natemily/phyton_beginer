n, a = int(input()), []
for i in range(n):
    a.append(int(input()))
del a[1::2]
print(a)
