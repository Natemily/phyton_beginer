line = input()
print(line.replace("@", ""))
for i in range(len(line)):
    if i % 3 != 0:
        print(line[i], end="")

