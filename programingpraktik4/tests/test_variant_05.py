"""Відкриті приклади 05 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(5)

PUBLIC = [('Іваненко;05.03;так\n'
  'Петренко;05.03;ні\n'
  'Іваненко;06.03;ні\n'
  'Петренко;06.03;Так\n'
  'Іваненко;07.03;так\n',
  'Записів: 5\n- Іваненко: 66%\n- Петренко: 50%\nВідсутностей: 2\nНекоректних рядків: 0'),
 (';05.03;так\n'
  'А;5.03;так\n'
  'А;05.3;так\n'
  'А;05.03;можливо\n'
  'А;05.03\n'
  'А;05.03;так;ще\n'
  '  Б ; 01.01 ; НІ \n',
  'Записів: 1\n- Б: 0%\nВідсутностей: 1\nНекоректних рядків: 6')]


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
