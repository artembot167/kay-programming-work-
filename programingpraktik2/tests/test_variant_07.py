"""Відкриті приклади 07 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(7)
solve = M.solve

PUBLIC = [
    (("3 1 3 2 1 4",), "Унікальні: 3 1 2 4\nВидалено: 2\nПовторювалися: 3 1"),
    (("5 6 7",), "Унікальні: 5 6 7\nВидалено: 0\nПовторювалися: немає")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
