# объявление функции
def is_palindrome(text):
    t = text.replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("-", "").lower()
    for i in range(0, len(t)):
        if t[i] != t[len(t) - 1 - i]:
            res = False
            break
        else:
            res = True
    return res

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
