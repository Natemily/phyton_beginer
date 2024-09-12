import random

list = []
digits = "23456789"
lowercase_letters = "abcdefghjkmnpqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKMNPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
punctuation2 = "il1Lo0O"
quantity_p = int(input('Какое будет количество паролей? '))
len_p = int(input('Длина пароля: '))
p_digits = input('Включать ли цифры 0123456789? (д=да/н=нет): ')
p_upper = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (д=да/н=нет): ')
p_lower = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (д=да/н=нет): ')
p_symbols1 = input('Включать ли символы !#$%&*+-=?@^_? (д=да/н=нет): ')
p_symbols2 = input('Исключать ли неоднозначные символы il1Lo0O? (д=да/н=нет): ')

for i in range(quantity_p):
    chars = ''
    while len(chars) < len_p:
        if p_digits == 'д':
            chars += random.choice(digits)
            if len(chars) == len_p:
                break
        if p_upper == 'д':
            chars += random.choice(uppercase_letters)
            if len(chars) == len_p:
                break
        if p_lower == 'д':
            chars += random.choice(lowercase_letters)   
            if len(chars) == len_p:
                break 
        if p_symbols1 == 'д':
            chars += random.choice(punctuation)
            if len(chars) == len_p:
                break
        if p_symbols2 == 'д':
            chars += random.choice(punctuation2)
            if len(chars) == len_p:
                break
    list.append(chars)

print("Ваши пароли:")
print(*list, sep='\n')