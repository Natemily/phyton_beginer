n, a, b = int(input()), [], []
for i in range(n):
    a.append(int(input()))
for i in range(len(a)):
    if a[i] < 0:
        b.append(a[i])
for i in range(len(a)):
    if a[i] == 0:
        b.append(a[i])
for i in range(len(a)):
    if a[i] > 0:
        b.append(a[i])     
print(*b, sep="\n")  