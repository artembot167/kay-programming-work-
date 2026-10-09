"""Відкриті приклади 01 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(1)

PUBLIC = [('10.0.0.1 GET /a 200 1024\n10.0.0.2 POST /b 404 2048\n10.0.0.3 GET /a 500 0\n',
  'Записів: 3\n'
  'Помилок (код 400 і вище): 2 (66.7%)\n'
  'Найпопулярніший шлях: /a (2)\n'
  'Трафік: 3.00 КБ\n'
  'Некоректних рядків: 0'),
 ('# коментар\n'
  '\n'
  '1.2.3 GET /a 200 1\n'
  '256.1.1.1 GET /a 200 1\n'
  '1.1.1.1 get /a 200 1\n'
  '1.1.1.1 GET a 200 1\n'
  '1.1.1.1 GET /a 99 1\n'
  '1.1.1.1 GET /a 600 1\n'
  '1.1.1.1 GET /a 200 x\n'
  '1.1.1.1 GET /a 200 1 extra\n',
  'Записів: 0\nНекоректних рядків: 8')]


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
