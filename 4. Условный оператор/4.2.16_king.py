x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if x1 == x2 and (y2 == y1 + 1 or y2 == y1 - 1) or y1 == y2 and (x2 == x1 + 1 or x2 == x1 - 1) or x2 == x1 + 1 and y2 == y1 + 1 or x2 == x1 - 1 and y2 == y1 - 1 or x2 == x1 + 1 and y2 == y1 - 1 or x2 == x1 - 1 and y2 == y1 + 1:
    print("YES")
else:
    print("NO")