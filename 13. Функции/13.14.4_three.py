# объявление функции
def draw_triangle():
    print(" "*(7)+"*")
    for i in range(7):
        print(" "*(6-i)+"*"*(i+2)+"*"*(i+1))

# основная программа
draw_triangle()  # вызов функции