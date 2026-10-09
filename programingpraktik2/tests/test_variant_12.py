"""Відкриті приклади 12 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(12)
solve = M.solve

PUBLIC = [
    (["3", "1 2 3 4 5"], "Суми блоків: 6, 9\nМаксимальна сума у блоці: 2"),
    (["2", "-1 5 10 -20 3"], "Суми блоків: 4, -10, 3\nМаксимальна сума у блоці: 1"),
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
