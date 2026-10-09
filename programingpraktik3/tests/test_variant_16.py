"""Відкриті приклади 16 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(16)
solve = M.solve

PUBLIC = [(('ab123 AB124 cd001 ab123', '2'),
  'Кодів: 4\n'
  'Унікальних кодів: 3\n'
  'Префікси за кількістю кодів (топ-2):\n'
  '1. AB: AB123, AB124, AB123\n'
  '2. CD: CD001'),
 (('123ab abc12 a1b23 ABCDE ab12', '3'), 'Помилка: немає даних')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
