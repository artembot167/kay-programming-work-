"""Відкриті приклади 22 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(22)
solve = M.solve

PUBLIC = [(('auth:120; db:300; auth:450; db:299', '2'),
  'Вимірів: 4\n'
  'Унікальних сервісів: 2\n'
  'Найповільніші сервіси (топ-2):\n'
  '1. auth: 450 мс\n'
  '2. db: 300 мс'),
 (('x:abc; y:-5; :10; z:0', '3'),
  'Вимірів: 1\nУнікальних сервісів: 1\nНайповільніші сервіси (топ-3):\n1. z: 0 мс')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
