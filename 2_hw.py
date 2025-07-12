from typing import Tuple
from typing import List

def task_1() -> Tuple[int, float, str, list, bool]:
    # Создаем переменные с указанием типов и произвольными значениями
    integer_var: int = 42
    float_var: float = 3.14
    string_var: str = "Hello, World!"
    list_var: list = [1, 2, 3, 4, 5]
    bool_var: bool = True

    # Выводим типы данных каждой переменной
    print(f"Тип integer_var: {type(integer_var)}")
    print(f"Тип float_var: {type(float_var)}")
    print(f"Тип string_var: {type(string_var)}")
    print(f"Тип list_var: {type(list_var)}")
    print(f"Тип bool_var: {type(bool_var)}")
    print(integer_var, float_var, string_var, list_var, bool_var)


    # Возвращаем значения переменных (по аннотации возвращаемых данных)
    return integer_var, float_var, string_var, list_var, bool_var

def task_2() -> List:
    # Создаем список
    a = [1, 2, 3, 5, 8, 13, 21]
    
    # Выводим первые 3 значения списка
    print(a[:3])
    print("Эта последовательность чисел называется числами Фибоначчи.")
    # Возвращаем список (по аннотации возвращаемых данных)
    return a
    
def task_3(number: int) -> int:
    # Возвращаем квадрат числа
    return number ** 2

# Ввод числа от пользователя
user_input = input("Введите число: ")

# Преобразуем введенное значение в целое число
try:
    number = int(user_input)
    # Вызов функции и вывод результата в консоль
    result = task_3(number)
    print(f"Квадрат числа {number} равен: {result}")
except ValueError:
    print("Ошибка: Введите целое число!")

# Вызов функции
task_1()
task_2()
