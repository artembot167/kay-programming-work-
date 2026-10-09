def solve(mass_str: str, distance_str: str) -> str:
    """
    Обчислює вартість доставки залежно від маси та відстані.
    """
    raise NotImplementedError  # TODO: реалізуйте розв'язок за карткою

if __name__ == "__main__":
    mass = input("Введіть масу (кг): ")
    distance = input("Введіть відстань (км): ")
    print(solve(mass, distance))
