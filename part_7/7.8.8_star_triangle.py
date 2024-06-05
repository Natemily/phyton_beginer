n = int(input())
mid = n // 2 + 1
for i in range(1, n+1):
    if i <= mid:
        for j in range(i):
            print("*", end="")
        print()
    elif i > mid:
        for j in range(mid-1, 0, -1):
            print("*", end="")
        print()
        mid -= 1
   