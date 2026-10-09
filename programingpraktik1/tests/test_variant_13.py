"""Відкриті приклади варіанта 13 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(13).solve

PUBLIC = [
    (("08:15",), "Частина доби: Ранок, Хвилин до півночі: 945"),
    (("25:00",), "Помилка: некоректний час")
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
