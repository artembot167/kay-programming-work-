"""Відкриті приклади 02 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(2)

PUBLIC = [('10:00:00 INFO Старт\n'
  '10:05:30 ERROR Збій\n'
  '10:06:00 warn мало\n'
  '11:00:00 WARN Диск\n'
  '12:59:59 ERROR Знову\n',
  'Записів: 4\n'
  'DEBUG: 0\n'
  'INFO: 1\n'
  'WARN: 1\n'
  'ERROR: 2\n'
  'Перша помилка: 10:05:30\n'
  'Остання помилка: 12:59:59\n'
  'Некоректних рядків: 1'),
 ('25:00:00 INFO a\n'
  '10:60:00 INFO a\n'
  '10:00:60 INFO a\n'
  '1:00:00 INFO a\n'
  '10:00 INFO a\n'
  '10:00:00 TRACE a\n'
  '10:00:00 INFO\n'
  '00:00:00 DEBUG ок\n'
  '23:59:59 INFO ok\n',
  'Записів: 2\nDEBUG: 1\nINFO: 1\nWARN: 0\nERROR: 0\nПомилок немає\nНекоректних рядків: 7')]


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
