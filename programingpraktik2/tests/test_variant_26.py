"""Відкриті приклади 26 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(26)
solve = M.solve

PUBLIC = [
    (["10 5 20", "2 10 1"], "Позиції: 20, 50, 20\nЗагальна сума: 90\nНайдорожча позиція: №2 (ціна 5, кількість 10, вартість 50)"),
    (["15", "3"], "Позиції: 45\nЗагальна сума: 45\nНайдорожча позиція: №1 (ціна 15, кількість 3, вартість 45)")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
