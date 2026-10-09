"""Відкриті приклади варіанта 17 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(17).solve

PUBLIC = [
    (("500", "8.0", "50", "45"), "Вартість: 2000.00 грн. Статус: вистачить"),
    (("800", "10.0", "45", "50"), "Вартість: 3600.00 грн. Статус: не вистачить, потрібно ще 30.00 л"),
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
