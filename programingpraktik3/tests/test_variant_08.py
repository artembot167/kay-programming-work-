"""Відкриті приклади 08 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(8)
solve = M.solve

PUBLIC = [(('Aab, bA! 123', '2'),
  'Літер: 5\nУнікальних літер: 2\nНайчастіші літери (топ-2):\n1. a: 3\n2. b: 2'),
 (('Привіт, світе', '3'),
  'Літер: 11\nУнікальних літер: 8\nНайчастіші літери (топ-3):\n1. в: 2\n2. т: 2\n3. і: 2')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
