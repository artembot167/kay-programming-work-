"""Відкриті приклади 29 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(29)
solve = M.solve

PUBLIC = [(('Картка:100; готівка:50; картка:25', '2'),
  'Платежів: 3\n'
  'Способів оплати: 2\n'
  'Способи оплати за сумою (топ-2):\n'
  '1. картка: 2 операцій, 125\n'
  '2. готівка: 1 операцій, 50'),
 (('чек:10; картка:x; :5; готівка', '3'), 'Помилка: немає даних')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
