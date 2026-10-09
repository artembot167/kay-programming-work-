"""Відкриті приклади 02 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(2)
solve = M.solve

PUBLIC = [
    (["2 5 8 1 3 0"], "Парні: 3, сума: 10\nНепарні: 3, сума: 9\nНайбільше парне: 8"),
    (["5 1 3"], "Парні: 0, сума: 0\nНепарні: 3, сума: 9\nНайбільше парне: немає")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
