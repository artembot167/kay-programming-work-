"""Відкриті приклади 07 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(7)
solve = M.solve

PUBLIC = [(('a.txt b.TXT c.py readme .gitignore end.', '2'),
  'Файлів: 6\n'
  'Унікальних розширень: 3\n'
  'Розширення за кількістю файлів (топ-2):\n'
  '1. без_розширення: readme, .gitignore, end.\n'
  '2. txt: a.txt, b.TXT'),
 (('x.tar.gz y.gz z', '3'),
  'Файлів: 3\n'
  'Унікальних розширень: 2\n'
  'Розширення за кількістю файлів (топ-3):\n'
  '1. gz: x.tar.gz, y.gz\n'
  '2. без_розширення: z')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
