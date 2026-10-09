"""Відкриті приклади 04 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(4)

PUBLIC = [('S1;21.5;40\nS2;-5;55\nS3;-31;55\nS4;50;10\nS5;50.1;0\n',
  'Записів: 5\n'
  'Середня температура: 17.1\n'
  'Максимальна вологість: 55 (S2)\n'
  'Аномалій: 2\n'
  'Некоректних рядків: 0'),
 (';1;1\nS;abc;1\nS;--1;1\nS;1.;1\nS;-;1\nS;1;101\nS;1;x\nS;1;\nS;1\nS;1;1;1\nS;-0.5;100\n',
  'Записів: 1\n'
  'Середня температура: -0.5\n'
  'Максимальна вологість: 100 (S)\n'
  'Аномалій: 0\n'
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
