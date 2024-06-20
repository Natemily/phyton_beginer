line = [int(i) for i in input().split()]
line.sort()
print(*line)
line.sort(reverse = True)
print(*line)
