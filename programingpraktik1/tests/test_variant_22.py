"""Відкриті приклади варіанта 22 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

solve = load(22).solve

PUBLIC = [
    (("1920", "1080"), "Мегапікселі: 2.07 Мп. Орієнтація: альбомна. Співвідношення: 16:9."),
    (("1000", "1000"), "Мегапікселі: 1.00 Мп. Орієнтація: квадратна. Співвідношення: 1:1.")
]


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_solve(args, expected):
    assert solve(*args) == expected
