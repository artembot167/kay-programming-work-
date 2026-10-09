def solve(temps_str: str) -> str:
    """
    Знаходить найдовший безперервний період строгого зростання температури.
    Повертає довжину періоду, позицію початку та різницю температур.
    """
    raise NotImplementedError  # TODO: реалізуйте розв'язок за карткою


if __name__ == "__main__":
    temps_input = input("Введіть температурні виміри: ")
    print(solve(temps_input))
