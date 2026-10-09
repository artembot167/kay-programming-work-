"""Відкриті приклади 09 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(9)
solve = M.solve

PUBLIC = [
    (("1 2 2 2 3 3",), "Серія: значення 2, довжина 3, позиція 2"),
    (("5 5 10 10 10 5 5 5",), "Серія: значення 10, довжина 3, позиція 3")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
