"""Відкриті приклади 28 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(28)

PUBLIC = [('101;стіл;25\n9;стілець;50\n101;шафа;5\n',
  'Записів: 3\n- 9: 50\n- 101: 30\nНайбільше предметів: 9\nНекоректних рядків: 0'),
 ('x;a;1\n1;;1\n1;a;0\n1;a;x\n1;a\n1;a;1;1\n-1;a;1\n007;a;2\n',
  'Записів: 1\n- 7: 2\nНайбільше предметів: 7\nНекоректних рядків: 7')]


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
