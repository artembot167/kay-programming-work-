"""Відкриті приклади варіанта 08 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(8).solve

PUBLIC = [
    (("95.5",), "Літера: A\nОцінка: Відмінно"),
    (("72",), "Літера: C\nОцінка: Задовільно"),
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
