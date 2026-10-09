"""Практична робота PP-P03. Варіант 07: Розширення файлів."""


def parse_items(text: str) -> list:
    """Розбирає вхідний рядок."""
    return text.split()


def build_index(items: list) -> dict:
    """Будує словник розширень файлів."""
    index = {}

    for item in items:
        if "." not in item or (
            item.startswith(".") and item.count(".") == 1
        ):
            ext = "без_розширення"
        else:
            ext = item.rsplit(".", 1)[1].lower()
            if ext == "":
                ext = "без_розширення"

        if ext not in index:
            index[ext] = []

        index[ext].append(item)

    return index


def rank(index: dict, n: int) -> list:
    """Повертає рейтинг розширень."""
    return sorted(
        index.items(),
        key=lambda x: (-len(x[1]), x[0])
    )[:max(0, n)]


def unique_sorted(items: list) -> list:
    """Повертає унікальні елементи за алфавітом."""
    return sorted(set(items))


def solve(text: str, n: str) -> str:
    """Формує підсумковий звіт."""
    items = parse_items(text)
    index = build_index(items)

    try:
        count = int(n)
    except ValueError:
        count = 0

    if count < 0:
        count = 0

    rating = rank(index, count)

    result = [
        f"Файлів: {len(items)}",
        f"Унікальних розширень: {len(index)}",
        f"Розширення за кількістю файлів (топ-{count}):"
    ]

    if not rating:
        result.append("немає")
    else:
        for i, (ext, files) in enumerate(rating, 1):
            result.append(
                f"{i}. {ext}: {', '.join(files)}"
            )

    return "\n".join(result)


if __name__ == "__main__":
    print(solve(input("Введіть текст: "), input("Введіть n: ")))
