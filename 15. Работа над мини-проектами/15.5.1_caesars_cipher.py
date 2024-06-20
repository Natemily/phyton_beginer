d = input("Шифруем или дешифруем? ш/д: ")
en_ru = input("Английский или русский? а/р: ")
step = int(input("Какой шаг сдвига? Целое число: "))
s = input('Введите сообщение: ')

lat_low = 'abcdefghijklmnopqrstuvwxyz'
lat_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
cyr_low = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
cyr_up = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def decypher(line, lang, step):
    decyphered_line = []
    if lang == "р":
        n = 32
        for el_r in line:
            if el_r in cyr_low:
                char = (cyr_low.index(el_r) - step) % n
                decyphered_line.append(cyr_low[char])
            elif el_r in cyr_up:
                char = (cyr_up.index(el_r) - step) % n
                decyphered_line.append(cyr_up[char])
            else:
                char = line.index(el_r)
                decyphered_line.append(el_r)
    elif lang == "а":
        n = 26
        for el_r in line:
            if el_r in lat_low:
                char = (lat_low.index(el_r) - step) % n
                decyphered_line.append(lat_low[char])
            elif el_r in lat_up:
                char = (lat_up.index(el_r) - step) % n
                decyphered_line.append(lat_up[char])
            else:
                decyphered_line.append(el_r)
    print(''.join(decyphered_line)) 
   
   
def cypher(line, lang, step):  
    cyphered_line = []
    if lang == "р":
        n = 32
        for el_r in line:
            if el_r in cyr_low:
                char = (cyr_low.index(el_r) + step) % n
                cyphered_line.append(cyr_low[char])
            elif el_r in cyr_up:
                char = (cyr_up.index(el_r) + step) % n
                cyphered_line.append(cyr_up[char])
            else:
                cyphered_line.append(el_r)
    elif lang == "а":
        n = 26
        for el_r in line:
            if el_r in lat_low:
                char = (lat_low.index(el_r) + step) % n
                cyphered_line.append(lat_low[char])
            elif el_r in lat_up:
                char = (lat_up.index(el_r) + step) % n
                cyphered_line.append(lat_up[char])
            else:
                cyphered_line.append(el_r)
    print(''.join(cyphered_line)) 

if d == 'ш':
     cypher(s, en_ru, step)
elif d == "д":
    decypher(s, en_ru, step)    