n, c = int(input()), 0
for i in range(n):
    line = input()
    if line.count("11") > 2:
        c += 1
print(c)