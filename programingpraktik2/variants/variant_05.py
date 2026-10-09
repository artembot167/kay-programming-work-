def solve(seq_str: str, k_str: str) -> str:
    """Обчислює ковзне середнє з вікном k і знаходить найкраще вікно."""
    raise NotImplementedError  # TODO: реалізуйте розв'язок за карткою

if __name__ == "__main__":
    seq = input("Введіть числа через пропуск: ")
    k = input("Введіть розмір вікна k: ")
    print(solve(seq, k))
