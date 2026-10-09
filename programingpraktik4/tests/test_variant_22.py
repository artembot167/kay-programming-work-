"""Відкриті приклади 22 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(22)

PUBLIC = [('n1;100.5;80\nn2;10;20\nn3;100.5;100.5\n',
  'Записів: 3\n'
  'Найбільший вхід: n1 (100.5)\n'
  'Середній вихід: 66.8\n'
  'Вихід більший за вхід: n2\n'
  'Некоректних рядків: 0'),
 (';1;1\nn;x;1\nn;1;x\nn;.5;1\nn;1;5.\nn;1\nn;1;1;1\nn;-1;1\nn;0;0\n',
  'Записів: 1\n'
  'Найбільший вхід: n (0.0)\n'
  'Середній вихід: 0.0\n'
  'Вихід більший за вхід: немає\n'
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
