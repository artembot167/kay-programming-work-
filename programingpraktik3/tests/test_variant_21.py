"""Відкриті приклади 21 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(21)
solve = M.solve

PUBLIC = [(('меч x 1; зілля x 3; Зілля x 2', '2'),
  'Записів: 3\n'
  'Унікальних предметів: 2\n'
  'Найбільші запаси (топ-2):\n'
  '1. зілля: 2 записів, разом 5\n'
  '2. меч: 1 записів, разом 1'),
 (('щит x ; x 5; лук x1; стріла x 10 x 2; ок x 7', '3'),
  'Записів: 1\nУнікальних предметів: 1\nНайбільші запаси (топ-3):\n1. ок: 1 записів, разом 7')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
