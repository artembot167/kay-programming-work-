"""Відкриті приклади варіанта 15 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(15).solve

PUBLIC = [
    (("12000", "40.0", "USD"), "До видачі: 297.00 USD (Комісія: 3.00 USD)"),
    (("5000", "42.5", "EUR"), "До видачі: 117.65 EUR (Комісія: 0.00 EUR)")
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
