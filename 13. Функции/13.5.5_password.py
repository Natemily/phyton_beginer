# объявление функции
def is_password_good(password):
    count1, count2, count3 = 0, 0, 0
    if len(password) >= 8:
        for i in range(len(password)):
            if password[i].isupper():
                count1 += 1
        for i in range(len(password)):    
            if password[i].islower():
                count2 += 1
        for i in range(len(password)):        
            if password[i].isdigit():
                count3 += 1
    if count1 >= 1 and count2 >= 1 and count3 >= 1:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))