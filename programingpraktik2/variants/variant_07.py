
def solve(items_str: str) -> str:
    numbers = list(map(int, items_str.split()))

    unique = []
    repeated = []
    seen = set()

    for number in numbers:
        if number not in seen:
            unique.append(number)
            seen.add(number)
        elif number not in repeated:
            repeated.append(number)

    removed = len(numbers) - len(unique)

    unique_text = " ".join(map(str, unique))
    repeated_text = " ".join(map(str, repeated))

    if not repeated:
        repeated_text = "немає"

    return (f"Унікальні: {unique_text}\n"
            f"Видалено: {removed}\n"
            f"Повторювалися: {repeated_text}")


if __name__ == "__main__":
    s = input("Введіть список цілих чисел: ")
    print(solve(s))
