n, s, s2 = int(input()), 1, 0
for i in range(1, n+1):
    s = s * i
    s2 += s 
print(s2)