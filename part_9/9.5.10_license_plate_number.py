line = input()
p = "АВЕКМНОРСТУХ"
if (len(line) == 9 or len(line) == 10) and line[0] in(p) and line[1:3].isdigit() and line[4] in(p) and line[5] in(p) and line[6] == "_" and line[7:10].isdigit():
    print("YES")
else:
    print('NO')