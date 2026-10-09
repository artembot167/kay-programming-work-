def solve(kwh: str, zone: str) -> str:
    """Обчислює вартість електроенергії."""
    raise NotImplementedError  # TODO: реалізуйте розв'язок за карткою

if __name__ == "__main__":
    kwh = input("Введіть обсяг споживання (кВт·год): ")
    zone = input("Введіть зону (день/ніч): ")
    print(solve(kwh, zone))
