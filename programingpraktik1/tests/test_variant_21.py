"""Відкриті приклади варіанта 21 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(21).solve

PUBLIC = [
    (("0.1",), "Бал: 0. Опис: Штиль."),
    (("15.0",), "Бал: 7. Опис: Міцний вітер.")
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
