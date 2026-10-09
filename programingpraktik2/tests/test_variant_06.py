"""Відкриті приклади 06 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(6)
solve = M.solve

PUBLIC = [
    (("1 3 5", "2 4 6"), "Злитий список: 1 2 3 4 5 6"),
    (("10 20", "5 15"), "Злитий список: 5 10 15 20")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
