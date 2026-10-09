"""Відкриті приклади 05 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(5)
solve = M.solve

PUBLIC = [(('Математика:90; Фізика:75; математика:80', '2'),
  'Оцінок: 3\n'
  'Унікальних предметів: 2\n'
  'Найвищі середні (топ-2):\n'
  '1. математика: 85.00\n'
  '2. фізика: 75.00'),
 (('a:101;b:100;c:0;d:-5;:50;e', '3'),
  'Оцінок: 2\nУнікальних предметів: 2\nНайвищі середні (топ-3):\n1. b: 100.00\n2. c: 0.00')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
