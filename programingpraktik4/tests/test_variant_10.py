"""Відкриті приклади 10 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(10)

PUBLIC = [('M1;100\nM2;50\nM1;130\nM2;40\nM1;150\n',
  'Записів: 5\n- M1: 50\n- M2: -10\nЗменшення показань: M2\nНекоректних рядків: 0'),
 (';5\nM;x\nM;-5\nM\nM;1;2\nM;7\nM;7\n',
  'Записів: 2\n- M: 0\nЗменшення показань: немає\nНекоректних рядків: 5')]


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
