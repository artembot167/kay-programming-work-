"""Відкриті приклади 26 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(26)

PUBLIC = [('Іваненко;Чат-бот;70\nПетренко;Гра;49\nСидоренко;Сайт;50\nПетренко;Гра;10\n',
  'Записів: 4\n'
  'Середня готовність: 44.8\n'
  'Нижче 50 %: Петренко\n'
  'Найвища готовність: 70\n'
  'Некоректних рядків: 0'),
 (';t;5\nа;;5\nа;t;101\nа;t;x\nа;t;-1\nа;t\nа;t;5;5\nа;t;100\nб;t;0\n',
  'Записів: 2\n'
  'Середня готовність: 50.0\n'
  'Нижче 50 %: б\n'
  'Найвища готовність: 100\n'
  'Некоректних рядків: 7')]


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
