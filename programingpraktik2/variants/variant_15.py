def solve(threshold_str: str, seq_str: str) -> str:
    """
    Додає квадрати парних чисел послідовності. Зупиняється, якщо сума перевищить поріг.
    Повертає фінальну суму, кількість оброблених елементів та факт перевищення порогу.
    """
    raise NotImplementedError  # TODO: реалізуйте розв'язок за карткою


if __name__ == "__main__":
    threshold_input = input("Введіть поріг: ")
    seq_input = input("Введіть послідовність чисел: ")
    print(solve(threshold_input, seq_input))
