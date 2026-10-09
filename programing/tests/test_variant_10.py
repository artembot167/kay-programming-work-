"""Відкриті приклади варіанта 10 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(10).solve

PUBLIC = [
    (("123456789",), "Рівень: слабкий\nБракує: літер"),
    (("myPass123",), "Рівень: сильний\nБракує: -"),
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
