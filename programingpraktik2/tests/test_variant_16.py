"""Відкриті приклади 16 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(16)
solve = M.solve

PUBLIC = [
    (["5"], "Перше число: 8\nНомер: 6\nПопередні: [1, 1, 2, 3, 5]"),
    (["100"], "Перше число: 144\nНомер: 12\nПопередні: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
