"""Відкриті приклади 13 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(13)

PUBLIC = [('Динамо;2;Шахтар;1\nШахтар;0;Зоря;0\nЗоря;3;Динамо;3\n',
  'Записів: 3\n1. Динамо — 4\n2. Зоря — 2\n3. Шахтар — 1\nГолів забито: 9\nНекоректних рядків: 0'),
 (';1;б;1\nа;1;;1\nа;1;а;1\nа;x;б;1\nа;1;б;-1\nа;1;б\nа;1;б;1;1\nа;1;б;2\n',
  'Записів: 1\n1. б — 3\n2. а — 0\nГолів забито: 3\nНекоректних рядків: 7')]


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
