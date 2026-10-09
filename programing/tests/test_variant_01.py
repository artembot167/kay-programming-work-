"""Відкриті приклади варіанта 01 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(1).solve

PUBLIC = [
    (("65", "170"), "ІМТ: 22.5, Категорія: Нормальна маса"),
    (("abc", "170"), "Помилка: некоректні дані")
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
