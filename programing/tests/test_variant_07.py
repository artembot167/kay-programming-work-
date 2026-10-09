"""Відкриті приклади варіанта 07 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(7).solve

PUBLIC = [
    (("8000",), "Податок: 400.00 грн\nЧистий дохід: 7600.00 грн\nЕфективна ставка: 5.0%"),
    (("25000",), "Податок: 2000.00 грн\nЧистий дохід: 23000.00 грн\nЕфективна ставка: 8.0%"),
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
