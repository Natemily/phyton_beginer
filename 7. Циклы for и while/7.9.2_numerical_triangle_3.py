n = int(input())
a = 0
for i in range(1, n+1):
    for j in range(i):
        if j <= i // 2 + 1:
            print(j, end="")
        elif j > i // 2 + 1:
            print(j, end="")
        print()


        print(a, end=" ")
        a += 1
    print()