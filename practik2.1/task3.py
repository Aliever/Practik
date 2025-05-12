def contains_duplicate(nums):
    seen = []  #пустой список для отслеживания встреченных чисел
    for num in nums:
        if num in seen:  # проверяем, есть ли число в списке
            return True
        seen.append(num)  # Если нет, добавляем число в список
    return False

# Примеры использования:
numbers = [1, 1, 3, 5, 6]
print(contains_duplicate(numbers))

