"""Відкриті приклади 24 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(24)
solve = M.solve

PUBLIC = [(('київ>львів; київ>одеса; львів>київ; київ>львів', '2'),
  'Рейсів: 4\n'
  'Унікальних пунктів: 3\n'
  'Пункти за кількістю напрямків (топ-2):\n'
  '1. Київ: Львів, Одеса\n'
  '2. Львів: Київ'),
 (('a>b>c; >x; y>; z', '3'), 'Помилка: немає даних')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
