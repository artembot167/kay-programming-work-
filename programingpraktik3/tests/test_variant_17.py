"""Відкриті приклади 17 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(17)
solve = M.solve

PUBLIC = [(('олена, Іван, ОЛЕНА,іван ,Іван', '2'),
  'Голосів: 5\nКандидатів: 2\nЛідери голосування (топ-2):\n1. Іван: 3\n2. Олена: 2'),
 ((', ,,', '3'), 'Помилка: немає даних')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
