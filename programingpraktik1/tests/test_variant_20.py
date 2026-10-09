"""Відкриті приклади варіанта 20 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(20).solve

PUBLIC = [
    (("3,4", "6,6"), "Г1: 7 (звичайний), Г2: 12 (критичний успіх). Переможець: Гравець 2"),
    (("1,1", "2,2"), "Г1: 2 (критичний провал), Г2: 4 (дубль). Переможець: Гравець 2"),
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
