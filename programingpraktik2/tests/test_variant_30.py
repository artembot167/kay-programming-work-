"""Відкриті приклади 30 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(30)
solve = M.solve

PUBLIC = [
    (["2 6 18 54"], "Тип: Геометрична\nЗнаменник: 3\nНаступний член: 162"),
    (["10 15 20 25"], "Тип: Арифметична\nРізниця: 5\nНаступний член: 30")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
