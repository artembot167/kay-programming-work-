"""Відкриті приклади 14 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(14)
solve = M.solve

PUBLIC = [(('S1: Коваль Іван, Шевченко Олег; S2: Коваль Іван', '2'),
  'Статей: 2\n'
  'Унікальних авторів: 2\n'
  'Найпродуктивніші автори (топ-2):\n'
  '1. Коваль Іван: 2\n'
  '2. Шевченко Олег: 1'),
 (('x:; :a; y: , ; z: Ім Ім, Ім Ім', '3'),
  'Статей: 1\nУнікальних авторів: 1\nНайпродуктивніші автори (топ-3):\n1. Ім Ім: 1')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
