def duplicate(nums):
    a = []  #пустой список для отслеживания встреченных чисел
    for num in nums:
        if num in a:  # проверяем, есть ли число в списке
            return True
        a.append(num)  # Если нет, добавляем число в список

    return False

numbers = [1, 1, 3, 5, 6]
print(duplicate(numbers))