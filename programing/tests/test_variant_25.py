"""Відкриті приклади варіанта 25 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(25).solve

PUBLIC = [
    (("10.5",), "Категорія: Добре. Рекомендація: Без ризиків."),
    (("100.0",), "Категорія: Нездорово. Рекомендація: Уникати тривалого перебування на вулиці.")
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
