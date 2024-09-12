n, a = int(input()), []
for i in range(n):
    a.append(int(input()))
for i in range(len(a)):
    if a[i] == max(a):
        mx = i
    elif a[i] == min(a):
        mn = i
if mx > mn:
    del a[mx]
    del a[mn]
else:
    del a[mn]
    del a[mx]
print(*a, sep="\n")