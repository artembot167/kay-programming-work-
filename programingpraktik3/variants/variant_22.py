"""Практична робота PP-P03. Варіант 22: Метрики сервісів.

Реалізуйте п'ять функцій за карткою варіанта. Введення й виведення — лише в блоці __main__.
"""


def parse_items(text: str) -> list:
    """Розбирає вхідний рядок і нормалізує елементи за правилами картки."""
    raise NotImplementedError  # TODO: реалізуйте за карткою


def build_index(items: list) -> dict:
    """Будує словник-індекс за правилом картки."""
    raise NotImplementedError  # TODO: реалізуйте за карткою


def rank(index: dict, n: int) -> list:
    """Повертає n найкращих пар (ключ, значення) як список кортежів."""
    raise NotImplementedError  # TODO: реалізуйте за карткою


def unique_sorted(items: list) -> list:
    """Повертає унікальні елементи, відсортовані за правилом картки."""
    raise NotImplementedError  # TODO: реалізуйте за карткою


def solve(text: str, n: str) -> str:
    """Збирає звіт за шаблоном картки."""
    raise NotImplementedError  # TODO: реалізуйте за карткою


if __name__ == "__main__":
    print(solve(input("Введіть текст: "), input("Введіть n: ")))
