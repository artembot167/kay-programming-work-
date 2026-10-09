"""Відкриті приклади варіанта 14 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(14).solve

PUBLIC = [
    (("1500.00", "так", ""), "До оплати: 1350.00 грн (Знижка: 10%)"),
    (("6000", "ні", "SAVE5"), "До оплати: 5100.00 грн (Знижка: 15%)")
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
