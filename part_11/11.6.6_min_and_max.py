line = input().split()
line2 = []
for i in range(len(line)):
    line2.append(int(line[i]))
imn = line2.index(min(line2))
imx = line2.index(max(line2))
line2[imn], line2[imx] = max(line2), min(line2)
print(*line2)
