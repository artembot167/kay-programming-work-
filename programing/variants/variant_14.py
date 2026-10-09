"""
Практична робота: Базові типи даних та умовні конструкції.
Варіант 14. Знижки магазину.
"""

def solve(amount_str: str, has_card: str, coupon: str) -> str:
    raise NotImplementedError  # TODO: реалізуйте розв'язок за карткою

if __name__ == "__main__":
    amt = input("Введіть суму чека: ")
    card = input("Чи є картка лояльності (так/ні): ")
    coup = input("Введіть купон (або залиште порожнім): ")
    print(solve(amt, card, coup))
