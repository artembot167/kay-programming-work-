"""Відкриті приклади 11 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(11)
solve = M.solve

PUBLIC = [
    (["1 3 2 4 1"], "Кількість піків: 2\nПозиції: 2, 4\nНайвищий пік: 4"),
    (["5 4 3 2 1"], "Кількість піків: 0"),
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
