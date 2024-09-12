day, weight = int(input()), float(input())
if 100-day*0.2 < weight:
    print("Что-то пошло не так")
else:
    print("Все идет по плану")
print(f"#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {100-day*0.2} кг")