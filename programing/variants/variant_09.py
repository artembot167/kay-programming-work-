def solve(category_str: str, quantity_str: str) -> str:
    """
    Розраховує загальну вартість квитків зі знижкою.
    """
    raise NotImplementedError  # TODO: реалізуйте розв'язок за карткою

if __name__ == "__main__":
    category = input("Введіть категорію квитка: ")
    quantity = input("Введіть кількість: ")
    print(solve(category, quantity))
