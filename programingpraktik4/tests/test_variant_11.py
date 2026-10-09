"""Відкриті приклади 11 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(11)

PUBLIC = [('a.zip;1048576;1\nb.zip;2097152;0\nc.zip;524288;1\n',
  'Записів: 3\n'
  'Успішних: 2\n'
  'Обсяг успішних: 1.50 МБ\n'
  'Найбільший файл: b.zip (2097152)\n'
  'Некоректних рядків: 0'),
 (';5;1\na;x;1\na;5;2\na;5;yes\na;5\na;5;1;1\nb;0;0\n',
  'Записів: 1\n'
  'Успішних: 0\n'
  'Обсяг успішних: 0.00 МБ\n'
  'Найбільший файл: b (0)\n'
  'Некоректних рядків: 6')]


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
