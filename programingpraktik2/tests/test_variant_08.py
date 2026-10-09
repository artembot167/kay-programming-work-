"""Відкриті приклади 08 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(8)
solve = M.solve

PUBLIC = [
    (("1 2 3 4 5", "2", "вліво"), "Результат зсуву: 3 4 5 1 2"),
    (("1 2 3 4 5", "1", "вправо"), "Результат зсуву: 5 1 2 3 4")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
