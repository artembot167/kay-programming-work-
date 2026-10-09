"""
Варіант 18. Простий кредит.
Розраховує щомісячний платіж, переплату за простими відсотками та категорію кредиту.
"""

def solve(amount_str: str, rate_str: str, months_str: str) -> str:
    raise NotImplementedError  # TODO: реалізуйте розв'язок за карткою

if __name__ == "__main__":
    a = input("Введіть суму кредиту: ")
    r = input("Введіть річну ставку (%): ")
    m = input("Введіть кількість місяців: ")
    print(solve(a, r, m))
