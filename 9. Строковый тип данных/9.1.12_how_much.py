line, a, b = input(), 0, 0
for i in range(0, len(line)):
    if line[i] == "+":
        a += 1
    elif line[i] == "*":
        b += 1
print('Символ + встречается', a, "раз")
print('Символ * встречается', b, "раз")