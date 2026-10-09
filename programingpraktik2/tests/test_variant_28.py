"""Відкриті приклади 28 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(28)
solve = M.solve

PUBLIC = [
    (["1 2 3 4 5"], "Середнє: 3.00\nВідкинуто: 2\nРезультат: 3 4 5"),
    (["10 10 10"], "Середнє: 10.00\nВідкинуто: 0\nРезультат: 10 10 10")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
