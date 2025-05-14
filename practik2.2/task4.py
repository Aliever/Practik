class Counter:
    def __init__(self, value=0):
        self.value = value #сохраняем значение в свойство обьекта


    def increase(self):
        self.value += 1

    def decrease(self):
        self.value -= 1

    def get_value(self):
        return self.value

# Демонстрация работы счётчика
counter = Counter()  # начальное значение 0

while True:
    print("\nТекущее значение счётчика:", counter.get_value())
    print("Меню:")
    print("1 - Увеличить на 1")
    print("2 - Уменьшить на 1")
    print("3 - Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        counter.increase()
    elif choice == "2":
        counter.decrease()
    elif choice == "3":
        print("Программа завершена.")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")