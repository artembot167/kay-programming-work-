"""Відкриті приклади варіанта 12 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(12).solve

PUBLIC = [
    (("-4",), "Знак: Від'ємне, Парність: Парне, Кратність: Немає"),
    (("15",), "Знак: Додатне, Парність: Непарне, Кратність: FizzBuzz")
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
