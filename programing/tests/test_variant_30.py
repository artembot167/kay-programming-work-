"""Відкриті приклади варіанта 30 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(30).solve

PUBLIC = [
    (("50", "день"), "До сплати: 132.00 грн"),
    (("150", "ніч"), "До сплати: 240.00 грн")
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
