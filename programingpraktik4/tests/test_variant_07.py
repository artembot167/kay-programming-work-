"""Відкриті приклади 07 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(7)

PUBLIC = [('a;помилка;1.1.1.1\na;помилка;1.1.1.1\nb;успіх;1.1.1.1\na;помилка;1.1.1.1\nb;помилка;2.2.2.2\n',
  'Записів: 5\nУспішних: 1\nПомилкових: 4\nПідозрілі: a\nНекоректних рядків: 0'),
 (';успіх;1.1.1.1\n'
  'a;можливо;1.1.1.1\n'
  'a;успіх;1.1.1\n'
  'a;успіх;256.1.1.1\n'
  'a;успіх;1.1.1.x\n'
  'a;успіх\n'
  'z;помилка;0.0.0.0\n'
  'z;помилка;255.255.255.255\n'
  'z;Помилка;0.0.0.0\n',
  'Записів: 3\nУспішних: 0\nПомилкових: 3\nПідозрілі: z\nНекоректних рядків: 6')]


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
