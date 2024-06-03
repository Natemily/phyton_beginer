a, b, c = input(), input(), input()
len_a, len_b, len_c = len(a), len(b), len(c)
max, min = max(len_a, len_b, len_c), min(len_a, len_b, len_c)
mid = len_a + len_b + len_c - max - min
if mid - min == (max - min) / 2:
    print('YES')
else:
    print('NO')