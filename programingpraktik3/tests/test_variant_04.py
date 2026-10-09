"""Відкриті приклади 04 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(4)
solve = M.solve

PUBLIC = [(('Яблука:10; груші:5; яблука:3', '2'),
  'Записів: 3\nУнікальних товарів: 2\nНайбільші залишки (топ-2):\n1. яблука: 13\n2. груші: 5'),
 (('x:1;y:abc;:5;z;w:2:3;q:4', '3'),
  'Записів: 2\nУнікальних товарів: 2\nНайбільші залишки (топ-3):\n1. q: 4\n2. x: 1')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
