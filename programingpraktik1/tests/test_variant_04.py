"""Відкриті приклади варіанта 04 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(4).solve

PUBLIC = [
    (("3665",), "1 год 01 хв 05 с"),
    (("305",), "5 хв 05 с")
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
