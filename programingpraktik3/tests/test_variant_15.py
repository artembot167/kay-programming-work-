"""Відкриті приклади 15 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(15)
solve = M.solve

PUBLIC = [(('0 5 6 11 12 17 18 23', '2'),
  'Відвідувань: 8\n'
  'Унікальних годин: 8\n'
  'Найзавантаженіші частини доби (топ-2):\n'
  '1. вечір: 2\n'
  '2. день: 2'),
 (('24 99 abc -1 7 7', '4'),
  'Відвідувань: 2\nУнікальних годин: 1\nНайзавантаженіші частини доби (топ-4):\n1. ранок: 2')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
