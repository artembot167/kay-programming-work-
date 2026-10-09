"""Відкриті приклади 02 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(2)
solve = M.solve

PUBLIC = [(('Ранок #Python і #python та #Kyiv', '2'),
  'Хештегів: 3\nУнікальних хештегів: 2\nПопулярні теги (топ-2):\n1. python: 2\n2. kyiv: 1'),
 (('без тегів # ще # тут', '3'), 'Помилка: немає даних')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
