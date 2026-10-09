"""
Практична робота: Базові типи даних та умовні конструкції.
Варіант 15. Обмін валют.
"""

def solve(amount_str: str, rate_str: str, currency: str) -> str:
    raise NotImplementedError  # TODO: реалізуйте розв'язок за карткою

if __name__ == "__main__":
    amt = input("Введіть суму в грн: ")
    rate = input("Введіть курс: ")
    curr = input("Введіть валюту (USD/EUR/PLN): ")
    print(solve(amt, rate, curr))
