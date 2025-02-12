def task_1() -> None:
    # Создаем переменные разных типов
    integer_var: int = 42
    float_var: float = 3.14
    string_var: str = "Hello, World!"
    list_var: list = [1, 2, 3, 4, 5]
    bool_var: bool = True

    # Выводим их типы в консоль
    print(f"integer_var: {type(integer_var)}")
    print(f"float_var: {type(float_var)}")
    print(f"string_var: {type(string_var)}")
    print(f"list_var: {type(list_var)}")
    print(f"bool_var: {type(bool_var)}")

# Вызов функции
task_1()
