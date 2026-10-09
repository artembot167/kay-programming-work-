"""Відкриті приклади варіанта 28 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(28).solve

PUBLIC = [
    (("2", "1", "ні"), "До сплати: 300.00 грн"),
    (("1.5", "6", "ні"), "До сплати: 375.00 грн")
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
