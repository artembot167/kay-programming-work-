"""Відкриті приклади 18 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(18)
solve = M.solve

PUBLIC = [(('5:100; 12:50; 5:20; 31:170', '2'),
  'Платежів: 4\nУнікальних днів: 3\nНайвитратніші дні (топ-2):\n1. 31: 170\n2. 5: 120'),
 (('0:10; 32:5; 7:x; 7; 10:1', '3'),
  'Платежів: 1\nУнікальних днів: 1\nНайвитратніші дні (топ-3):\n1. 10: 1')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
