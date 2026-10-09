"""Відкриті приклади 21 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(21)
solve = M.solve

PUBLIC = [
    (["10 15 12 -5 0"], "Різниці: [5, -3, -17, 5]\nНайбільший стрибок: -17 (позиція 2)"),
    (["4 4 4"], "Різниці: [0, 0]\nНайбільший стрибок: 0 (позиція 0)")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
