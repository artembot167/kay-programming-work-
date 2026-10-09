"""Відкриті приклади 27 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(27)

PUBLIC = [('10:30;72\n10:31;49\n10:32;121\n10:33;50\n10:34;120\n',
  'Записів: 5\nМінімум: 49\nМаксимум: 121\nСередній: 82.4\nПоза 50..120: 2\nНекоректних рядків: 0'),
 ('24:00;70\n'
  '10:60;70\n'
  '1:00;70\n'
  '10:00;29\n'
  '10:00;221\n'
  '10:00;x\n'
  '10:00\n'
  '10:00;70;1\n'
  '10:00;30\n'
  '23:59;220\n',
  'Записів: 2\n'
  'Мінімум: 30\n'
  'Максимум: 220\n'
  'Середній: 125.0\n'
  'Поза 50..120: 2\n'
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
