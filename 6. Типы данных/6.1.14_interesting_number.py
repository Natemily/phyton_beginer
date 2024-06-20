nml = int(input())
l = nml % 10
m = (nml % 100) // 10
n = nml // 100
max = max(l, n, m)
min = min(l, n, m)
med = l + m + n - max - min
if max - min == med:
    print("Число интересное")
else:
    print("Число неинтересное")