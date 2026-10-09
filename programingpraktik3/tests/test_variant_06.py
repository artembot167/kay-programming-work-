"""Відкриті приклади 06 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(6)
solve = M.solve

PUBLIC = [(('їжа:120.5; транспорт:30; їжа:79.5', '2'),
  'Витрат: 3\n'
  'Унікальних категорій: 2\n'
  'Найбільші витрати (топ-2):\n'
  '1. їжа: 200.00\n'
  '2. транспорт: 30.00'),
 (('x:1.2.3;y:.5;z:5.;w:abc;v:7', '3'),
  'Витрат: 1\nУнікальних категорій: 1\nНайбільші витрати (топ-3):\n1. v: 7.00')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
