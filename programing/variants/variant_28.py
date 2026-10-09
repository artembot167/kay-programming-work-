import math

def solve(hours: str, day: str, is_student: str) -> str:
    """Обчислює вартість оренди обладнання."""
    raise NotImplementedError  # TODO: реалізуйте розв'язок за карткою

if __name__ == "__main__":
    hours = input("Введіть кількість годин: ")
    day = input("Введіть день тижня (1-7): ")
    is_student = input("Чи є студентський (так/ні): ")
    print(solve(hours, day, is_student))
