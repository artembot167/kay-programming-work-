"""Відкриті приклади варіанта 03 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(3).solve

PUBLIC = [
    (("1", "-3", "2"), "D = 1.000, Корені: 1.000, 2.000"),
    (("0", "2", "-4"), "Лінійне рівняння, Корінь: 2.000")
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
