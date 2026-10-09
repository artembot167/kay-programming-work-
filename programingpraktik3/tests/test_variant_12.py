"""Відкриті приклади 12 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(12)
solve = M.solve

PUBLIC = [(('d1: кіт пес; d2: кіт ліс; d3: Кіт', '2'),
  'Пар «документ-слово»: 5\n'
  'Унікальних слів: 3\n'
  'Слова за кількістю документів (топ-2):\n'
  '1. кіт: d1, d2, d3\n'
  '2. ліс: d2'),
 (('a: x x y; b; :c; e: z: w', '3'),
  'Пар «документ-слово»: 3\n'
  'Унікальних слів: 2\n'
  'Слова за кількістю документів (топ-3):\n'
  '1. x: a\n'
  '2. y: a')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
