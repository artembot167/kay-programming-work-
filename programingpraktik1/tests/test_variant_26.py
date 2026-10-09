"""Відкриті приклади варіанта 26 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(26).solve

PUBLIC = [
    (("прямокутник", "2", "3", ""), "Площа: 6.00, Периметр: 10.00"),
    (("коло", "1", "", ""), "Площа: 3.14, Периметр: 6.28")
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
