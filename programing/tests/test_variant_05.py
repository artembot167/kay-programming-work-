"""Відкриті приклади варіанта 05 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(5).solve

PUBLIC = [
    (("20.06",), "68.1 °F, 293.2 K, Стан: рідина"),
    (("-300",), "Помилка: температура нижче абсолютного нуля")
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
