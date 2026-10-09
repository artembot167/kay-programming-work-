"""Відкриті приклади 11 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(11)
solve = M.solve

PUBLIC = [(('+380671234567 0671234567 0501112233', '2'),
  'Номерів: 3\nУнікальних кодів: 2\nНайпоширеніші коди (топ-2):\n1. 67: 2\n2. 50: 1'),
 (('12345 +38067123456 0671234 +3806712345678 abc +380a12345678 067123456x', '3'),
  'Помилка: немає даних')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
