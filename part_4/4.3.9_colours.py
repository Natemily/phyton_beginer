k, m = input(), input()
if k == 'красный':
    if m == 'синий':
        print('фиолетовый')
    elif m == 'желтый':
        print('оранжевый')
    elif m == 'красный':
        print('красный')
    else:
        print('ошибка цвета')
elif k == 'синий':
    if m == 'желтый':
        print("зеленый")
    elif m == 'красный':
        print('фиолетовый')
    elif m == 'синий':
        print('синий')
    else:
        print('ошибка цвета')
elif k == 'желтый':
    if m == 'красный':
        print('оранжевый')
    elif m == 'синий':
        print("зеленый")
    elif m == 'желтый':
        print("желтый")
    else:
        print('ошибка цвета')
else:
        print('ошибка цвета')