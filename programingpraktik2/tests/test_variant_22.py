"""Відкриті приклади 22 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(22)
solve = M.solve

PUBLIC = [
    (["1 2 3", "4 -5 6"], "Скалярний добуток: 12\nСуми стовпців: [5, -3, 9]\nМаксимальна сума: 9 (позиція 2)"),
    (["10", "10"], "Скалярний добуток: 100\nСуми стовпців: [20]\nМаксимальна сума: 20 (позиція 0)")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
