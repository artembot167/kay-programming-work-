"""Практична робота PP-P04. Варіант 07: Журнал входів."""




def parse_entry(line: str) -> dict | None:
    parts = line.strip().split(";")

    if len(parts) != 3:
        return None

    user, result, ip = [p.strip() for p in parts]
    result = result.lower()

    if not user or result not in ("успіх", "помилка"):
        return None

    ip_parts = ip.split(".")

    if len(ip_parts) != 4:
        return None

    for part in ip_parts:
        if not part.isdigit():
            return None

        number = int(part)

        if number < 0 or number > 255:
            return None

    return {
        "user": user,
        "result": result,
        "ip": ip
    }




def read_entries(path: str) -> tuple[list[dict], int]:
    """Читає журнал із файлу."""
    entries = []
    skipped = 0

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            entry = parse_entry(line)

            if entry is None:
                skipped += 1
            else:
                entries.append(entry)

    return entries, skipped


def build_report(entries: list[dict], skipped: int) -> str:
    """Формує звіт за журналом."""
    success = 0
    errors = 0
    user_errors = {}

    for entry in entries:
        if entry["result"] == "успіх":
            success += 1
        else:
            errors += 1
            user = entry["user"]
            user_errors[user] = user_errors.get(user, 0) + 1

    suspicious = sorted(
        user for user, count in user_errors.items()
        if count >= 3
    )

    return (
        f"Записів: {len(entries)}\n"
        f"Успішних: {success}\n"
        f"Помилкових: {errors}\n"
        f"Підозрілі: {', '.join(suspicious)}\n"
        f"Некоректних рядків: {skipped}"
    )


def process(path: str) -> str:
    """Читає файл і повертає звіт."""
    try:
        entries, skipped = read_entries(path)
    except FileNotFoundError:
        return "Помилка: файл не знайдено"

    return build_report(entries, skipped)


if __name__ == "__main__":
    print(process(input("Введіть шлях до файла журналу: ")))
