"""Відкриті приклади 19 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(19)
solve = M.solve

PUBLIC = [(('Alpha#web#api; Beta#web; Gamma#API#ui', '2'),
  'Пар «проєкт-тег»: 5\n'
  'Унікальних тегів: 3\n'
  'Теги за кількістю проєктів (топ-2):\n'
  '1. api: Alpha, Gamma\n'
  '2. web: Alpha, Beta'),
 (('#x#y; w##; v#z#Z', '3'),
  'Пар «проєкт-тег»: 2\nУнікальних тегів: 1\nТеги за кількістю проєктів (топ-3):\n1. z: v')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
