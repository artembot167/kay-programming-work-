"""Відкриті приклади 15 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(15)
solve = M.solve

PUBLIC = [
    (["20", "1 4 3 4 5"], "Сума квадратів: 32\nОброблено елементів: 4\nПеревищення порогу: Так"),
    (["50", "2 -2 5"], "Сума квадратів: 8\nОброблено елементів: 3\nПеревищення порогу: Ні"),
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
