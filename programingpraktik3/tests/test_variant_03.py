"""Відкриті приклади 03 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(3)
solve = M.solve

PUBLIC = [(('Anna@Mail.com; bob@mail.com; kate@ukr.net', '2'),
  'Адрес: 3\n'
  'Унікальних доменів: 2\n'
  'Домени за кількістю адрес (топ-2):\n'
  '1. mail.com: anna, bob\n'
  '2. ukr.net: kate'),
 (('bad; a@@b.c; @x.y; z@; ok@d.org', '5'),
  'Адрес: 1\nУнікальних доменів: 1\nДомени за кількістю адрес (топ-5):\n1. d.org: ok')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
