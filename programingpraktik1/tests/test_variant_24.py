"""Відкриті приклади варіанта 24 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(24).solve

PUBLIC = [
    (("3.5", "1.2", "2.0"), "Порядок: 1.2, 2.0, 3.5. Статус: усі різні. Медіана: 2.0."),
    (("5.0", "5.0", "5.0"), "Порядок: 5.0, 5.0, 5.0. Статус: усі рівні. Медіана: 5.0.")
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
