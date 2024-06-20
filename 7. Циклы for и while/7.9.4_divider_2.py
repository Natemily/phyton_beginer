n = int(input())
for i in range(1, n+1):
    k = 0
    p = 0
    for j in range(1, i+1):
        if i % j == 0:
            k = i
            p += 1
    print(k, "+"*p, sep="")
print()