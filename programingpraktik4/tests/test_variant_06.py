"""Відкриті приклади 06 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(6)

PUBLIC = [('A-1;прихід;10\nB-2;прихід;5\nA-1;видача;3\nB-2;видача;8\n',
  "Записів: 4\n- A-1: 7\n- B-2: -3\nВід'ємних залишків: 1\nНекоректних рядків: 0"),
 (';прихід;1\n'
  'A;повернення;1\n'
  'A;прихід;0\n'
  'A;прихід;-1\n'
  'A;прихід;x\n'
  'A;прихід\n'
  'A;ПРИХІД;4\n'
  'A;видача;4\n',
  "Записів: 2\n- A: 0\nВід'ємних залишків: 0\nНекоректних рядків: 6")]


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
