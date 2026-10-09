"""Відкриті приклади варіанта 02 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(2).solve

PUBLIC = [
    (("3", "4", "5"), "Тип: Різносторонній, Прямокутний: Так"),
    (("1", "10", "12"), "Помилка: трикутник не існує")
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
