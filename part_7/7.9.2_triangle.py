n, a = int(input()), 1

for i in range(n):
    for j in range(a):
        print(j + 1, end = "")
    for k in range(a - 1, 0, -1):
        print(k, end = "")
    a += 1
    print()
        