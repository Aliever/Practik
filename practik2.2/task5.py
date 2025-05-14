class MyClass:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
        print("Объект создан:", self.a, self.b)

    def show(self):
        print("a =", self.a)
        print("b =", self.b)

    def dell(self):
        print("Объект удалён:", self.a, self.b)


obj = None

while True:
    print("\nМеню:")
    print("1. Создать объект по умолчанию")
    print("2. Создать объект с параметрами")
    print("3. Показать значения объекта")
    print("4. Удалить объект")
    print("5. Выход")

    choice = input("Выберите пункт меню (1-5): ")

    if choice == "1":
        obj = MyClass()

    elif choice == "2":
        a = int(input("Введите значение a: "))
        b = int(input("Введите значение b: "))
        obj = MyClass(a, b)

    elif choice == "3":
        if obj:
            obj.show()
        else:
            print("Сначала создайте объект!")

    elif choice == "4":
        if obj:
            del obj
            obj = None
            print("Объект удалён.")
        else:
            print("Объекта нет для удаления.")

    elif choice == "5":
        print("Выход из программы.")
        if obj:
            del obj
        break

    else:
        print("Некорректный ввод. Попробуйте снова.")


