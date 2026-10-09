"""Відкриті приклади 24 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(24)
solve = M.solve

PUBLIC = [
    (["10 20 30"], "Нормалізовані дані: [0.0, 0.5, 1.0]"),
    (["5 5 5"], "Помилка: вироджений випадок (усі значення однакові).")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
