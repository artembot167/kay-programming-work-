"""Відкриті приклади 27 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(27)
solve = M.solve

PUBLIC = [(('Іван:95; Олена:75; Петро:59; Марія:90; Іван:60', '2'),
  'Записів: 5\n'
  'Унікальних студентів: 4\n'
  'Літерні оцінки за кількістю студентів (топ-2):\n'
  '1. A: Іван, Марія\n'
  '2. B: Олена'),
 (('x:101; :50; y:abc; z', '3'), 'Помилка: немає даних')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
