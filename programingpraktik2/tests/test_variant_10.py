"""Відкриті приклади 10 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(10)
solve = M.solve

PUBLIC = [
    (("2 4 1 5", "7"), "Префіксні суми: 2 6 7 12\nПоріг 7 досягнуто на позиції 3"),
    (("1 2 3", "10"), "Префіксні суми: 1 3 6\nПоріг 10 не досягнуто")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
