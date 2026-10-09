"""Відкриті приклади 17 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(17)
solve = M.solve

PUBLIC = [
    (["Python is a powerful programming language", "p"], "Найдовше слово: programming\nСлів на літеру 'p': 3\nЗа алфавітом: ['Python', 'a', 'is', 'language', 'powerful', 'programming']"),
    (["Apple banana Apricot cherry", "a"], "Найдовше слово: Apricot\nСлів на літеру 'a': 2\nЗа алфавітом: ['Apple', 'Apricot', 'banana', 'cherry']")
]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected
