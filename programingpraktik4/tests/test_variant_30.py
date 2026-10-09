"""Відкриті приклади 30 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(30)

PUBLIC = [('05.03;дохід;1000\n06.03;Витрата;250.50\n07.03;витрата;1000\n',
  'Записів: 3\n'
  'Дохід: 1000.00\n'
  'Витрати: 1250.50\n'
  'Баланс: -250.50\n'
  'Доходів: 1\n'
  'Витрат: 2\n'
  'Некоректних рядків: 0'),
 ('5.03;дохід;1\n'
  '05.03;борг;1\n'
  '05.03;дохід;0\n'
  '05.03;дохід;x\n'
  '05.03;дохід;.5\n'
  '05.03;дохід;5.\n'
  '05.03;дохід\n'
  '05.03;дохід;1;1\n'
  '05.03;дохід;0.5\n',
  'Записів: 1\n'
  'Дохід: 0.50\n'
  'Витрати: 0.00\n'
  'Баланс: 0.50\n'
  'Доходів: 1\n'
  'Витрат: 0\n'
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
