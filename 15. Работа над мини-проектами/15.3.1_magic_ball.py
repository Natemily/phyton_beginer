import random

answers = ['Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова', 'Даже не думай', 'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений', 'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да', 'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие', 'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input("Напишите свое имя: ")
print(f"Здравствуй, {name}")

flag = True

while flag == True:
    q = input("Напишите вопрос, который вас волнует: ")
    print(f"Магический шар глаголет: {random.choice(answers)}")
    a = input("Желаете задать еще один вопрос? ")
    if a.lower() == 'да':
        flag = True
    else:
        print('Возвращайся если возникнут вопросы!')
        flag = False