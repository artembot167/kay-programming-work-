"""Відкриті приклади 08 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(8)

PUBLIC = [('0671234567;125;вхідний\n0501112233;3600;вихідний\n0671234567;60;Вхідний\n',
  'Записів: 3\n'
  'Загальна тривалість: 01:03:05\n'
  'Середня тривалість: 1261.7 с\n'
  'вхідний: 2\n'
  'вихідний: 1\n'
  'Некоректних рядків: 0'),
 ('067123456;10;вхідний\n'
  '06712345678;10;вхідний\n'
  '067123456a;10;вхідний\n'
  '0671234567;0;вхідний\n'
  '0671234567;x;вхідний\n'
  '0671234567;10;пропущений\n'
  '0671234567;10\n',
  'Записів: 0\nНекоректних рядків: 7')]


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
