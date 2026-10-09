"""Відкриті приклади 05 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(5)
solve = M.solve

PUBLIC = [
    (["1 2 3 4 5", "3"], "Середні: 2.0 3.0 4.0\nНайкраще вікно: 3"),
    (["10 20", "3"], "Помилка: некоректний розмір вікна")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
