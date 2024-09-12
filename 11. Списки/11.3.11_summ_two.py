n, b, c = int(input()), [], []
for i in range(n):
    a = int(input())
    b.append(a)
for i in range(len(b)):
    if i != len(b)-1:
        c.append(b[i]+b[i+1])
print(c)