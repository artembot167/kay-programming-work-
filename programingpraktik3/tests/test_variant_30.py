"""Відкриті приклади 30 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(30)
solve = M.solve

PUBLIC = [(('a.txt A.doc b.txt a.pdf', '2'),
  'Файлів: 4\n'
  'Унікальних основ: 2\n'
  'Групи за кількістю файлів (топ-2):\n'
  '1. a: a.txt, A.doc, a.pdf\n'
  '2. b: b.txt'),
 (('data data.csv .env env. x.y.z x.y', '3'),
  'Файлів: 6\n'
  'Унікальних основ: 5\n'
  'Групи за кількістю файлів (топ-3):\n'
  '1. data: data, data.csv\n'
  '2. .env: .env\n'
  '3. env.: env.')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
