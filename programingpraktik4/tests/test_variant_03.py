"""Відкриті приклади 03 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(3)

PUBLIC = [('05.03;120.50;Їжа\n06.03;30;транспорт\n07.03;120.50;їжа\n',
  'Записів: 3\n'
  'Сума: 271.00\n'
  'Найбільший платіж: 120.50 (їжа)\n'
  'За категоріями:\n'
  '- транспорт: 30.00\n'
  '- їжа: 241.00\n'
  'Некоректних рядків: 0'),
 ('32.01;5;a\n'
  '01.13;5;a\n'
  '1.01;5;a\n'
  '01.01;0;a\n'
  '01.01;0.0;a\n'
  '01.01;.5;a\n'
  '01.01;5.;a\n'
  '01.01;5;\n'
  '01.01;5\n'
  '01.01;5;a;b\n'
  '01.01;1.5;a\n'
  '31.12;2;b\n',
  'Записів: 2\n'
  'Сума: 3.50\n'
  'Найбільший платіж: 2.00 (b)\n'
  'За категоріями:\n'
  '- a: 1.50\n'
  '- b: 2.00\n'
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
