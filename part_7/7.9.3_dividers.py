a, b = int(input()), int(input())
s_i, x_i = -1, -1

for i in range (a, b+1):
    s = 0
    x = 0
    
    for j in range (1, i+1):
        if i % j == 0:
            s += j
    
    if s_i <= s:
        s_i = s
        x_i = i      

print(x_i, s_i)