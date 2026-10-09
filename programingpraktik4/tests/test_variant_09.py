"""Відкриті приклади 09 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(9)

PUBLIC = [('Іваненко;Математика;85\nІваненко;Фізика;60\nПетренко;Математика;59\nПетренко;Фізика;100\n',
  'Записів: 4\n'
  '- Іваненко: 72.50\n'
  '- Петренко: 79.50\n'
  'Найкращий: Петренко\n'
  'Балів нижче 60: 1\n'
  'Некоректних рядків: 0'),
 (';м;5\nа;;5\nа;м;101\nа;м;-1\nа;м;x\nа;м\nа;м;50;1\nб;м;0\n',
  'Записів: 1\n- б: 0.00\nНайкращий: б\nБалів нижче 60: 1\nНекоректних рядків: 7')]


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
