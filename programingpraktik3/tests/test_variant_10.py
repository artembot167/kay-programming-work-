"""Відкриті приклади 10 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(10)
solve = M.solve

PUBLIC = [(('україна-київ; україна-львів; польща-краків; Україна-київ', '2'),
  'Записів: 4\n'
  'Унікальних міст: 3\n'
  'Країни за кількістю міст (топ-2):\n'
  '1. Україна: Київ, Львів\n'
  '2. Польща: Краків'),
 (('a-b-c; -x; y-; z-w', '3'),
  'Записів: 1\nУнікальних міст: 1\nКраїни за кількістю міст (топ-3):\n1. Z: W')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
