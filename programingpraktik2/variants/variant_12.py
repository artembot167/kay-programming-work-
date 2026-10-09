def solve(k_str: str, seq_str: str) -> str:
    """
    Розбиває послідовність на блоки розміру k, обчислює суму кожного блоку та знаходить блок із максимальною сумою.
    """
    raise NotImplementedError  # TODO: реалізуйте розв'язок за карткою


if __name__ == "__main__":
    k_input = input("Введіть розмір блоку: ")
    seq_input = input("Введіть послідовність чисел: ")
    print(solve(k_input, seq_input))
