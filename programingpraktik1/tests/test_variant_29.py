"""Відкриті приклади варіанта 29 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(29).solve

PUBLIC = [
    (("10", "95.5", "0"), "Бал: 120, Категорія: Відмінно"),
    (("5", "85.0", "1"), "Бал: 45, Категорія: Потребує покращення")
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
