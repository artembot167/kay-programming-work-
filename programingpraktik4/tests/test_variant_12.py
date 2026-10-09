"""Відкриті приклади 12 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(12)

PUBLIC = [('A1;250;17.5\nB2;100;9\nA1;250;12.5\n',
  'Записів: 3\n'
  '- A1: 6.00 л/100км\n'
  '- B2: 9.00 л/100км\n'
  'Найекономніше: A1\n'
  'Сумарний пробіг: 600 км\n'
  'Некоректних рядків: 0'),
 (';5;1\nA;0;1\nA;x;1\nA;5;0\nA;5;0.0\nA;5;.5\nA;5;5.\nA;5;1.5.5\nA;5\nA;5;1;1\nA;100;5\n',
  'Записів: 1\n'
  '- A: 5.00 л/100км\n'
  'Найекономніше: A\n'
  'Сумарний пробіг: 100 км\n'
  'Некоректних рядків: 10')]


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
