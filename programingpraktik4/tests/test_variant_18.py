"""Відкриті приклади 18 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(18)

PUBLIC = [('05.03;Біг;45;400\n06.03;плавання;30;300\n07.03;біг;15;100\n',
  'Записів: 3\n'
  'Хвилин: 90\n'
  'Калорій: 800\n'
  'Найкалорійніше: біг (400)\n'
  '- біг: 60\n'
  '- плавання: 30\n'
  'Некоректних рядків: 0'),
 ('5.03;a;1;1\n'
  '05.03;;1;1\n'
  '05.03;a;0;1\n'
  '05.03;a;1;0\n'
  '05.03;a;x;1\n'
  '05.03;a;1\n'
  '05.03;a;1;1;1\n'
  '05.03;йога;20;80\n',
  'Записів: 1\n'
  'Хвилин: 20\n'
  'Калорій: 80\n'
  'Найкалорійніше: йога (80)\n'
  '- йога: 20\n'
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
