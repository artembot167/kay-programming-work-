"""Відкриті приклади варіанта 06 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(6).solve

PUBLIC = [
    (("1.5", "50"), "Вартість доставки: 50.00 грн"),
    (("5.0", "120.5"), "Вартість доставки: 121.25 грн"),
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
