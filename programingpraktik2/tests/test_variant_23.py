"""Відкриті приклади 23 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(23)
solve = M.solve

PUBLIC = [
    (["2 7 11 15 2 7", "9"], "Перша пара: (2, 7) на позиціях (0, 1)\nКількість пар: 4"),
    (["1 2 3", "10"], "Пар немає")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
