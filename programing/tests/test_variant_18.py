"""Відкриті приклади варіанта 18 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(18).solve

PUBLIC = [
    (("12000", "10.0", "12"), "Платіж: 1100.00, переплата: 1200.00. Категорія: низьке"),
    (("5000", "25.0", "6"), "Платіж: 937.50, переплата: 625.00. Категорія: високе"),
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
