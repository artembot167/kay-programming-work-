"""Відкриті приклади 14 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(14)

PUBLIC = [('1;5;Чудово\n2;4;\n3;5; ок; чудово \n4;1;Погано\n',
  'Записів: 4\n'
  'Розподіл: 1:1 2:0 3:0 4:1 5:2\n'
  'Середня оцінка: 3.75\n'
  'Без тексту: 1\n'
  'Некоректних рядків: 0'),
 ('x;5;t\n1;0;t\n1;6;t\n1;x;t\n1;5\n;5;t\n-1;5;t\n1;3;\n',
  'Записів: 1\n'
  'Розподіл: 1:0 2:0 3:1 4:0 5:0\n'
  'Середня оцінка: 3.00\n'
  'Без тексту: 1\n'
  'Некоректних рядків: 7')]


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
