def solve(pm25: str) -> str:
    """Визначає категорію якості повітря та рекомендацію."""
    raise NotImplementedError  # TODO: реалізуйте розв'язок за карткою

if __name__ == "__main__":
    val = input("PM2.5 (мкг/м³): ")
    print(solve(val))
