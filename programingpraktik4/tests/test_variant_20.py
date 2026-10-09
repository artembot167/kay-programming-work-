"""Відкриті приклади 20 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(20)

PUBLIC = [('USD;39.50;40.10\nEUR;42;43.5\nUSD;39.6;40.3\n',
  'Записів: 3\n- EUR: 1.500\n- USD: 0.700\nНайбільший спред: EUR\nНекоректних рядків: 0'),
 ('usd;1;2\n'
  'US;1;2\n'
  'USDD;1;2\n'
  'УСД;1;2\n'
  'USD;0;2\n'
  'USD;2;1\n'
  'USD;1;1\n'
  'USD;x;2\n'
  'USD;1\n'
  'USD;1;2;3\n'
  'US1;1;2\n'
  'PLN;9.5;9.6\n',
  'Записів: 1\n- PLN: 0.100\nНайбільший спред: PLN\nНекоректних рядків: 11')]


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
