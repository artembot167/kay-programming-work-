"""Відкриті приклади 09 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(9)
solve = M.solve

PUBLIC = [(('info старт; error збій; INFO ок; warn мало місця', '2'),
  'Записів: 4\nУнікальних рівнів: 3\nНайчастіші рівні (топ-2):\n1. INFO: 2\n2. ERROR: 1'),
 (('TRACE x; fatal y; ; ', '3'), 'Помилка: немає даних')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
