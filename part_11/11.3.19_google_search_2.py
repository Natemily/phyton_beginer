n, a, b, c = int(input()), [], [], []
for i in range(n):
    a.append(input())
k = int(input())
for i in range(k):
    b.append(input())
    
for i in range(0, len(a)-1):
    for j in range(0, len(b)-1):
        if b[j].lower() in a[i].lower():
            c.append(a[i])
print(*c, sep="\n")