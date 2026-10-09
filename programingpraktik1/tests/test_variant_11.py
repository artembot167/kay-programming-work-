"""Відкриті приклади варіанта 11 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(11).solve

PUBLIC = [
    (("10", "3", "//"), "3"),
    (("5", "2.5", "*"), "12.5")
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
