"""Відкриті приклади 27 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(27)
solve = M.solve

PUBLIC = [
    (["Привіт, Світ 7777!"], "Голосних: 3\nПриголосних: 7\nЦифр: 4\nІнших: 4\nНайчастіша голосна: і (зустрічається 2 разів)"),
    (["qwrty 123"], "Голосних: 0\nПриголосних: 0\nЦифр: 3\nІнших: 6\nНайчастіша голосна: немає")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
