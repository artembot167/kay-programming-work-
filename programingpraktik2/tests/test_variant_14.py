"""Відкриті приклади 14 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(14)
solve = M.solve

PUBLIC = [
    (["1 2 3 2 4 5 6"], "Найдовший період зростання: 4 вимірів\nПочаткова позиція: 4\nПриріст: 4"),
    (["5 4 3"], "Періодів зростання не знайдено"),
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
