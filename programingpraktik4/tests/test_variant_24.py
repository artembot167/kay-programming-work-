"""Відкриті приклади 24 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(24)

PUBLIC = [('T1;2.5;доставлено\nT2;1;в дорозі\nT3;0.5;Втрачено\nT4;3.25;доставлено\n',
  'Записів: 4\n'
  'доставлено: 2\n'
  'в дорозі: 1\n'
  'втрачено: 1\n'
  'Вага доставлених: 5.8 кг\n'
  'Частка втрачених: 25.0%\n'
  'Некоректних рядків: 0'),
 (';1;доставлено\n'
  'T;0;доставлено\n'
  'T;x;доставлено\n'
  'T;.5;доставлено\n'
  'T;5.;доставлено\n'
  'T;1;невідомо\n'
  'T;1\n'
  'T;1;доставлено;1\n'
  'T;0.1;в дорозі\n',
  'Записів: 1\n'
  'доставлено: 0\n'
  'в дорозі: 1\n'
  'втрачено: 0\n'
  'Вага доставлених: 0.0 кг\n'
  'Частка втрачених: 0.0%\n'
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
