"""Відкриті приклади 23 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(23)
solve = M.solve

PUBLIC = [(('кіт Тік кто ток кот', '2'),
  'Слів: 5\n'
  'Унікальних слів: 5\n'
  'Найбільші групи анаграм (топ-2):\n'
  '1. кот: кот, кто, ток\n'
  '2. кті: кіт, тік'),
 (('a1 b2 ab ba AB', '3'),
  'Слів: 3\nУнікальних слів: 2\nНайбільші групи анаграм (топ-3):\n1. ab: ab, ba')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
