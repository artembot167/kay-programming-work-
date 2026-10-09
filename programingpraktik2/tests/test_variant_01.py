"""Відкриті приклади 01 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(1)
solve = M.solve

PUBLIC = [
    (["85 90 75 100 60"], "Кількість: 5\nСума: 410\nСереднє: 82.0\nМінімум: 60\nМаксимум: 100\nВище середнього: 3"),
    (["101 90"], "Помилка: некоректні дані")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
