"""Відкриті приклади 04 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(4)
solve = M.solve

PUBLIC = [
    (["1 2 3 2 1"], "Розвернуто: 1 2 3 2 1\nПаліндром: так"),
    (["4 -5 7"], "Розвернуто: 7 -5 4\nПаліндром: ні")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
