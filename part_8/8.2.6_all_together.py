n, a_3, c_end, c_4, c_5, p_7, c_15 = int(input()), 0, 0, 0, 0, 1, 0
end = n % 10
while n > 0:
    if n % 10 == 3:
        a_3 += 1
    if n % 10 == end:
        c_end += 1
    if n % 2 == 0:
        c_4 += 1
    if n % 10 > 5:
        c_5 += n % 10
    if n % 10 > 7:
        p_7 *= n % 10
    if n % 10 == 0 or n % 10 == 5:
        c_15 += 1
    n //= 10
print(a_3, c_end, c_4, c_5, p_7, c_15, sep="\n")