"""Відкриті приклади 01 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(1)
solve = M.solve

PUBLIC = [(('Кіт біжить, кіт спить! Пес біжить.', '2'),
  'Слів: 6\nУнікальних слів: 4\nНайчастіші слова (топ-2):\n1. біжить: 2\n2. кіт: 2'),
 (('a A a, b? B b b.', '3'),
  'Слів: 7\nУнікальних слів: 2\nНайчастіші слова (топ-3):\n1. b: 4\n2. a: 3')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
