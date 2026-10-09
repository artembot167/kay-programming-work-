"""Відкриті приклади 26 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(26)
solve = M.solve

PUBLIC = [(('Борщ: буряк, Картопля, сіль; Суп: картопля, сіль, Сіль', '2'),
  'Пар «страва-інгредієнт»: 6\n'
  'Унікальних інгредієнтів: 3\n'
  'Найуживаніші інгредієнти (топ-2):\n'
  '1. картопля: 2\n'
  '2. сіль: 2'),
 ((':х; y; z: , ; w: a:b', '3'), 'Помилка: немає даних')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
