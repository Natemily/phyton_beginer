for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            for l in range(1, 100):
                if i**3 + j**3 == k**3 + l**3 and i != k and i != l and j != k and j != l:
                    print(i, j, k, l, i**3 + j**3)