"""Відкриті приклади 03 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(3)
solve = M.solve

PUBLIC = [
    (["4 1 7 4 7 5"], "Друге найбільше: 5, позиція: 6"),
    (["3 3 3"], "Помилка: недостатньо унікальних значень")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
