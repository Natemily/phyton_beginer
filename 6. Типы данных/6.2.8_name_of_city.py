a, b, c = input(), input(), input()
len_a, len_b, len_c = len(a), len(b), len(c)
max, min = max(len_a, len_b, len_c), min(len_a, len_b, len_c)

if max == len_a:
    d = a
elif max == len_b:
    d = b
else:
    d = c
if min == len_a:
    e = a
elif min == len_b:
    e = b
else:
    e = c
    
print(e, d, sep='\n')