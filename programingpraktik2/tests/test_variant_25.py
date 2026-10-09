"""Відкриті приклади 25 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(25)
solve = M.solve

PUBLIC = [
    (["4 1 2 4 3 1"], "Медіана: 2.5\nМода: 1"),
    (["7 9 7 2 7"], "Медіана: 7.0\nМода: 7")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
