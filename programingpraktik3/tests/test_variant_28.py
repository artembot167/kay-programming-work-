"""Відкриті приклади 28 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(28)
solve = M.solve

PUBLIC = [(('великий=величезний; великий=значний; Малий=крихітний', '2'),
  'Пар: 3\n'
  'Унікальних слів: 5\n'
  'Слова за кількістю синонімів (топ-2):\n'
  '1. великий: величезний, значний\n'
  '2. величезний: великий'),
 (('a=a; =b; c=; d=e=f; g', '3'), 'Помилка: немає даних')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
