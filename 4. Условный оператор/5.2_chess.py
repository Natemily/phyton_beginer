a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a % 2 != 0 and b % 2 != 0 or a % 2 == 0 and b % 2 == 0:
    if c % 2 != 0 and d % 2 != 0 or c % 2 == 0 and d % 2 == 0:
        print("YES")
    else:
        print("NO")
elif a % 2 != 0 and b % 2 == 0 or a % 2 == 0 and b % 2 != 0:
    if c % 2 != 0 and d % 2 == 0 or c % 2 == 0 and d % 2 != 0:
        print('YES')
    else:
        print('NO')