"""Відкриті приклади варіанта 23 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(23).solve

PUBLIC = [
    (("80", "8", "40"), "До сплати: 150.00 грн. Перевищення: хв - 0, ГБ - 0, SMS - 0."),
    (("120", "12", "55"), "До сплати: 215.00 грн. Перевищення: хв - 20, ГБ - 2, SMS - 5.")
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
