"""Відкриті приклади 20 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(20)
solve = M.solve

PUBLIC = [(('Я йду, я бачу! Ти їси?', '2'),
  'Слів: 6\nУнікальних слів: 5\nДовжини за кількістю слів (топ-2):\n1. 3: йду, їси\n2. 1: я'),
 (('aa bb cc ddd ee fff', '3'),
  'Слів: 6\n'
  'Унікальних слів: 6\n'
  'Довжини за кількістю слів (топ-3):\n'
  '1. 2: aa, bb, cc, ee\n'
  '2. 3: ddd, fff')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
