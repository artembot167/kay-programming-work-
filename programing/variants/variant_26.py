import math

def solve(shape: str, p1: str, p2: str, p3: str) -> str:
    """Обчислює площу та периметр геометричної фігури."""
    raise NotImplementedError  # TODO: реалізуйте розв'язок за карткою

if __name__ == "__main__":
    shape = input("Введіть фігуру (коло, прямокутник, квадрат, трикутник): ")
    p1 = input("Введіть параметр 1: ")
    p2 = input("Введіть параметр 2 (якщо є): ")
    p3 = input("Введіть параметр 3 (якщо є): ")
    print(solve(shape, p1, p2, p3))
