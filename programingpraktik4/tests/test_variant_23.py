"""Відкриті приклади 23 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(23)

PUBLIC = [('H1;1200;60\nH2;900;30\nH1;1500;60\n',
  'Записів: 3\n'
  '- H1: 25.00 кВт·год/м²\n'
  '- H2: 30.00 кВт·год/м²\n'
  'Найвитратніший: H2\n'
  'Середнє: 27.50\n'
  'Некоректних рядків: 0'),
 (';1;1\nH;x;1\nH;1;x\nH;1;0\nH;1;0.0\nH;.5;1\nH;1;5.\nH;1\nH;1;1;1\nH;0;10\n',
  'Записів: 1\n- H: 0.00 кВт·год/м²\nНайвитратніший: H\nСереднє: 0.00\nНекоректних рядків: 9')]


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
