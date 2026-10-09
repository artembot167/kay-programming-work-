"""Відкриті приклади 18 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(18)
solve = M.solve

PUBLIC = [
    (["Hello World", "3"], "Зашифрований текст: Khoor Zruog"),
    (["abc XYZ", "-1"], "Зашифрований текст: zab WXY")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
