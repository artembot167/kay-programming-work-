"""Відкриті приклади 21 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(21)

PUBLIC = [('A1;250.50;брак\nA2;100;Брак\nA3;40.25;не підійшло\n',
  'Записів: 3\n'
  '- брак: 2 шт., 350.50\n'
  '- не підійшло: 1 шт., 40.25\n'
  'Загальна сума: 390.75\n'
  'Некоректних рядків: 0'),
 (';5;a\nA;0;a\nA;x;a\nA;.5;a\nA;5.;a\nA;5;\nA;5\nA;5;a;b\nA;0.5;a\n',
  'Записів: 1\n- a: 1 шт., 0.50\nЗагальна сума: 0.50\nНекоректних рядків: 8')]


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
