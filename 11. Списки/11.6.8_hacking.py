n, mes = int(input()[1:]), []
for i in range(n):
    mes.append(input())

for i in range(n):
    if "#" in mes[i]:
        index = mes[i].find("#")
        line_new = mes[i][:index].rstrip()
        mes[i] = line_new

print(*mes, sep='\n')
