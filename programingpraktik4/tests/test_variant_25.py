"""Відкриті приклади 25 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(25)

PUBLIC = [('Борщ;40;55.50\nКомпот;100;10\nБорщ;10;55.50\n',
  'Записів: 3\n'
  '1. Борщ — 2775.00\n'
  '2. Компот — 1000.00\n'
  'Найпопулярніша: Компот (100)\n'
  'Середня виручка на страву: 1887.50\n'
  'Некоректних рядків: 0'),
 (';5;1\nA;0;1\nA;x;1\nA;5;x\nA;5;.5\nA;5;5.\nA;5\nA;5;1;1\nA;5;0\n',
  'Записів: 1\n'
  '1. A — 0.00\n'
  'Найпопулярніша: A (5)\n'
  'Середня виручка на страву: 0.00\n'
  'Некоректних рядків: 8')]


def run(content, tmp_path):
    path = tmp_path / "journal.log"
    path.write_text(content, encoding="utf-8")
    return M.process(str(path))


@pytest.mark.parametrize("content,expected", PUBLIC)
def test_public(tmp_path, content, expected):
    assert run(content, tmp_path) == expected


def test_functions_exist():
    for name in ('parse_entry', 'read_entries', 'build_report', 'process'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
