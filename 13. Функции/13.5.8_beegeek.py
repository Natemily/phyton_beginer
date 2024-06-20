def is_palindrome(text):
    for i in range(0, len(text)):
        if text[i] != text[len(text) - 1 - i]:
            res = False
            break
        else:
            res = True
    return res

def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num != 1 and num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


# объявление функции
def is_valid_password(password):
    password = password.split(':')
    res = False
    if len(password) == 3:
        if is_palindrome(password[1]) and is_prime(int(password[2])) and int(password[3]) % 2 == 0:
            res = True
    return res

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))