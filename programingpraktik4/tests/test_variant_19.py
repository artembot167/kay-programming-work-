"""Відкриті приклади 19 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(19)

PUBLIC = [('Квест;12;150.50\nКонцерт;100;20\nЛекція;30;0\n',
  'Записів: 3\n'
  'Загальна вартість: 3806.00\n'
  'Найбільша подія: Концерт (2000.00)\n'
  'Середня кількість учасників: 47.3\n'
  'Некоректних рядків: 0'),
 (';5;1\nA;0;1\nA;x;1\nA;5;x\nA;5;.5\nA;5;5.\nA;5\nA;5;1;1\nA;5;0\n',
  'Записів: 1\n'
  'Загальна вартість: 0.00\n'
  'Найбільша подія: A (0.00)\n'
  'Середня кількість учасників: 5.0\n'
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
