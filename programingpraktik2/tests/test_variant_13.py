"""Відкриті приклади 13 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(13)
solve = M.solve

PUBLIC = [
    (["100", "+50 -200 +100"], "Фінальний баланс: -50\nВиконано операцій: 2\nЗупинка: Так"),
    (["0", "+10 +20"], "Фінальний баланс: 30\nВиконано операцій: 2\nЗупинка: Ні"),
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
