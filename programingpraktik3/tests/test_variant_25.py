"""Відкриті приклади 25 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(25)
solve = M.solve

PUBLIC = [(('Вхід:готово; Звіт:в роботі; Тест:ГОТОВО; Вхід:новий', '2'),
  'Завдань: 4\n'
  'Унікальних завдань: 3\n'
  'Статуси за кількістю завдань (топ-2):\n'
  '1. готово: Вхід, Тест\n'
  '2. в роботі: Звіт'),
 (('a:закрито; :новий; b; c:новий:x', '3'), 'Помилка: немає даних')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
