age = int(input())
if age <= 13:
    print('детство')
else:
    if age <= 24:
        print('молодость')
    else:
        if age <= 59:
            print('зрелость')
        else:
            print('старость')