from itertools import combinations #юзал чтоб генерить комбинации

def comb_sum(candidates, target):
    result = set()  #чтоб  хранить ток уникальные комбо

    for number in candidates:   # Проверяем одиночные элементы
        if number == target:
            result.add((number,))  # Добавляем одиночный элемент как кортеж

    # Генерируем комбинации разной длины
    for r in range(2, len(candidates) + 1):  # Начинаем с 2 до длины списка
        for combo in combinations(candidates, r):  #r определит какого размера будут генериться комбинации
            if sum(combo) == target:
                result.add(combo)  # Добавляем комбинацию в множество

    return list(result)  #множество => список

candidates = [1, 2, 2, 4, 5]
target = 5
combinations_found = comb_sum(candidates, target)
print(combinations_found)


