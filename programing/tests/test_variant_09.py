"""Відкриті приклади варіанта 09 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(9).solve

PUBLIC = [
    ((" Дитячий ", "6"), "До сплати: 270.00 грн"),
    (("ДОРОСЛИЙ", "2"), "До сплати: 240.00 грн"),
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
