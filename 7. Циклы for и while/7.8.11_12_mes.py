for a in range(26, 28):
    for b in range(83, 85):
        for c in range(109, 111):
            for d in range(132, 134):
                for e in range(143, 145):
                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                        print(a+b+c+d+e)
