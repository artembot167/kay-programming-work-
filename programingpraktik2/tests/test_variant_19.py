"""Відкриті приклади 19 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(19)
solve = M.solve

PUBLIC = [
    (["5 1 4 2 8"], "Відсортований список: [1, 2, 4, 5, 8]\nКількість порівнянь: 10\nКількість обмінів: 4"),
    (["-3 10 0 -1"], "Відсортований список: [-3, -1, 0, 10]\nКількість порівнянь: 6\nКількість обмінів: 3")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
