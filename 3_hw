# Задача 2: Нахождение наибольшего из двух чисел
def max_of_two():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print("Наибольшее число:", max(a, b))

# Задача 3: Проверка, отличаются ли числа на 135
def check_difference():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    if abs(a - b) == 135:
        print("yes")
    else:
        print("no")

# Задача 4: Определение сезона по номеру месяца
def get_season():
    month = int(input("Введите номер месяца (от 1 до 12): "))
    if month in [12, 1, 2]:
        print("зима")
    elif month in [3, 4, 5]:
        print("весна")
    elif month in [6, 7, 8]:
        print("лето")
    elif month in [9, 10, 11]:
        print("осень")
    else:
        print("Неверный номер месяца")

# Задача 5: Проверка, все ли числа больше 10
def all_greater_than_ten():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = float(input("Введите третье число: "))
    if a > 10 and b > 10 and c > 10:
        print("yes")
    else:
        print("no")

# Задача 6: Количество положительных чисел в списке
def count_positive_numbers():
    numbers = list(map(float, input("Введите 5 чисел через пробел: ").split()))
    if len(numbers) != 5:
        print("Нужно ввести ровно 5 чисел!")
        return
    count = sum(1 for num in numbers if num > 0)
    print("Количество положительных чисел:", count)

# Задача 7: Расчет количества дней за указанное количество лет и месяцев
def calculate_days():
    years = int(input("Введите количество лет: "))
    months = int(input("Введите количество месяцев: "))
    total_days = years * 12 * 29 + months * 29
    print("Общее количество дней:", total_days)

# Меню для выбора задачи
def main():
    while True:
        print("\nВыберите задачу:")
        print("1. Нахождение наибольшего из двух чисел")
        print("2. Проверка, отличаются ли числа на 135")
        print("3. Определение сезона по номеру месяца")
        print("4. Проверка, все ли числа больше 10")
        print("5. Количество положительных чисел в списке")
        print("6. Расчет количества дней за указанное количество лет и месяцев")
        print("0. Выход")
        choice = input("Введите номер задачи: ")

        if choice == "1":
            max_of_two()
        elif choice == "2":
            check_difference()
        elif choice == "3":
            get_season()
        elif choice == "4":
            all_greater_than_ten()
        elif choice == "5":
            count_positive_numbers()
        elif choice == "6":
            calculate_days()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    main()
