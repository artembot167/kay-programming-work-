def solve(balance_str: str, ops_str: str) -> str:
    """
    Застосовує операції до балансу. Зупиняється, якщо баланс стає від'ємним.
    Повертає фінальний стан рахунку, кількість операцій та факт зупинки.
    """
    raise NotImplementedError  # TODO: реалізуйте розв'язок за карткою


if __name__ == "__main__":
    balance_input = input("Введіть початковий баланс: ")
    ops_input = input("Введіть операції: ")
    print(solve(balance_input, ops_input))
