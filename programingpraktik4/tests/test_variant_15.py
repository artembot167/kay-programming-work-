"""Відкриті приклади 15 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(15)

PUBLIC = [('a;10:00;50\nb;10:00;91\na;11:00;90\nb;12:00;10\n',
  'Записів: 4\nМаксимум: 91% (b)\n- a: 70.0\n- b: 50.5\nПіки понад 90 %: b\nНекоректних рядків: 0'),
 (';10:00;5\n'
  'a;24:00;5\n'
  'a;10:60;5\n'
  'a;1:00;5\n'
  'a;10:00;101\n'
  'a;10:00;x\n'
  'a;10:00\n'
  'a;10:00;5;5\n'
  'a;23:59;100\n',
  'Записів: 1\nМаксимум: 100% (a)\n- a: 100.0\nПіки понад 90 %: a\nНекоректних рядків: 8')]


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
