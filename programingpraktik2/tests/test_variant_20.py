"""Відкриті приклади 20 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(20)
solve = M.solve

PUBLIC = [
    (["1 3 5 7 9 11", "7"], "Позиція: 4\nКількість кроків: 3"),
    (["-5 0 2 10", "4"], "Позиція: не знайдено\nКількість кроків: 3")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
