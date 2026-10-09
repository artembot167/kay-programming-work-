"""Відкриті приклади 29 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(29)
solve = M.solve

PUBLIC = [
    (["2 -3 4 0 5 -1"], "Змін знаку: 3\nСуворо знакочергувальна: Ні\nНайдовший відрізок: 3"),
    (["-1 2 -3 4"], "Змін знаку: 3\nСуворо знакочергувальна: Так\nНайдовший відрізок: 4")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
