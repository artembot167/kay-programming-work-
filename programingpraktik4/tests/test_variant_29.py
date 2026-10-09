"""Відкриті приклади 29 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(29)

PUBLIC = [('Вода;3;250.75\nгаз;3;400\nвода;4;200\n',
  'Записів: 3\n'
  '- вода: 450.75\n'
  '- газ: 400.00\n'
  'Найдорожча послуга: вода\n'
  'Середній платіж за місяць: 425.38\n'
  'Некоректних рядків: 0'),
 (';1;1\nв;0;1\nв;13;1\nв;x;1\nв;1;0\nв;1;x\nв;1;.5\nв;1;5.\nв;1\nв;1;1;1\nв;12;0.5\nв;1;1\n',
  'Записів: 2\n'
  '- в: 1.50\n'
  'Найдорожча послуга: в\n'
  'Середній платіж за місяць: 0.75\n'
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
