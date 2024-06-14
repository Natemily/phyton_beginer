n, a, b = int(input()), [], ''
for i in range(n):
    a.append(input())
k = int(input())
for i in range(len(a)):
    for j in range(len(a[i])):
        if j == k-1:
            b += a[i][j]
print(b)
