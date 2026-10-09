"""Практична робота PP-P04. Варіант 10: Показання лічильників.

Реалізуйте чотири функції за карткою варіанта. Введення й виведення — лише в блоці __main__.
"""


def parse_entry(line: str) -> dict | None:
    """Розбирає один рядок журналу; повертає словник або None для некоректного рядка."""
    raise NotImplementedError  # TODO: реалізуйте за карткою


def read_entries(path: str) -> tuple[list[dict], int]:
    """Читає файл рядками (with, utf-8); повертає (записи, кількість_некоректних)."""
    raise NotImplementedError  # TODO: реалізуйте за карткою


def build_report(entries: list[dict], skipped: int) -> str:
    """Формує звіт за шаблоном картки."""
    raise NotImplementedError  # TODO: реалізуйте за карткою


def process(path: str) -> str:
    """Читає файл і повертає звіт; для відсутнього файла — повідомлення про помилку."""
    raise NotImplementedError  # TODO: реалізуйте за карткою


if __name__ == "__main__":
    print(process(input("Введіть шлях до файла журналу: ")))
