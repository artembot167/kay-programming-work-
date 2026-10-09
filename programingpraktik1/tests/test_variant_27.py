"""Відкриті приклади варіанта 27 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(27).solve

PUBLIC = [
    ((" 42 ",), "Тип: ціле, Значення: 42, Тип Python: int"),
    (("ТАК",), "Тип: логічне, Значення: True, Тип Python: bool")
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
