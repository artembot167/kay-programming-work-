"""Відкриті приклади 16 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(16)

PUBLIC = [('Київ-Львів;450.50;3\nКиїв-Одеса;300;2\nКиїв-Львів;450.50;1\n',
  'Записів: 3\n'
  '- Київ-Львів: 1802.00\n'
  '- Київ-Одеса: 600.00\n'
  'Загальна виручка: 2402.00\n'
  'Найбільше квитків: Київ-Львів (4)\n'
  'Некоректних рядків: 0'),
 (';5;1\nA;0;1\nA;x;1\nA;5;0\nA;5;x\nA;.5;1\nA;5.;1\nA;5\nA;5;1;1\nA;0.5;2\n',
  'Записів: 1\n- A: 1.00\nЗагальна виручка: 1.00\nНайбільше квитків: A (2)\nНекоректних рядків: 9')]


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
