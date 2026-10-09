def solve(tasks: str, quality: str, penalty_days: str) -> str:
    """Обчислює бал та категорію активності."""
    raise NotImplementedError  # TODO: реалізуйте розв'язок за карткою

if __name__ == "__main__":
    tasks = input("Введіть кількість завдань: ")
    quality = input("Введіть відсоток якості (0-100): ")
    penalty_days = input("Введіть кількість днів запізнення: ")
    print(solve(tasks, quality, penalty_days))
