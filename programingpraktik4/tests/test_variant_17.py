"""Відкриті приклади 17 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(17)

PUBLIC = [('Z1;12.345;г\nZ2;1000;г\nZ3;1000.5;Г\nZ4;3;мл\n',
  'Записів: 4\n- г: 670.948\n- мл: 3.000\nПоза діапазоном 0..1000: 1\nНекоректних рядків: 0'),
 (';1;г\nZ;1;\nZ;x;г\nZ;.5;г\nZ;5.;г\nZ;-1;г\nZ;1\nZ;1;г;ще\nZ;0;г\n',
  'Записів: 1\n- г: 0.000\nПоза діапазоном 0..1000: 0\nНекоректних рядків: 8')]


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
