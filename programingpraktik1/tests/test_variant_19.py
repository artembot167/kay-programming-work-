"""Відкриті приклади варіанта 19 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(19).solve

PUBLIC = [
    (("2.5", "км"), "Довжина: 2500.000 м. Зручна одиниця: км"),
    (("45", "см"), "Довжина: 0.450 м. Зручна одиниця: см"),
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
