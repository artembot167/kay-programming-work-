"""Відкриті приклади варіанта 16 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(16).solve

PUBLIC = [
    (("30", "30"), "Швидкість: 60.0 км/год. Категорія: у межах"),
    (("150", "90"), "Швидкість: 100.0 км/год. Категорія: понад 20"),
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
