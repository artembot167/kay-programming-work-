"""
Варіант 17. Вартість поїздки.
Обчислює вартість пального на поїздку та перевіряє, чи вистачить одного повного бака.
"""

def solve(distance_str: str, consumption_str: str, price_str: str, tank_str: str) -> str:
    raise NotImplementedError  # TODO: реалізуйте розв'язок за карткою

if __name__ == "__main__":
    d = input("Введіть відстань (км): ")
    c = input("Введіть витрату пального (л/100 км): ")
    p = input("Введіть ціну літра (грн): ")
    t = input("Введіть ємність бака (л): ")
    print(solve(d, c, p, t))
