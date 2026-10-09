def solve(prices_str: str, counts_str: str) -> str:
    """
    Обчислює вартість позицій, суму та знаходить найдорожчу позицію.
    """
    raise NotImplementedError  # TODO: реалізуйте розв'язок за карткою

if __name__ == "__main__":
    prices = input("Введіть ціни (через пропуск): ")
    counts = input("Введіть кількості (через пропуск): ")
    print(solve(prices, counts))
