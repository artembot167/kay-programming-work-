
from pathlib import Path


def parse_line(line):
    parts = [p.strip() for p in line.strip().split(";")]

    if len(parts) != 5:
        return "Неправильна кількість полів (очікується 5)"

    code, destination, duration, delay, passengers = parts

    if not duration.isdigit() or int(duration) <= 0:
        return "Тривалість має бути додатним цілим числом"

    if not delay.isdigit():
        return "Затримка не може бути від'ємною"

    if not passengers.isdigit():
        return "Кількість пасажирів не може бути від'ємною"

    if (len(code) != 5 or not code[:2].isalpha()
            or not code[:2].isascii() or not code[:2].isupper()
            or not code[2:].isdigit()
            or not code[2:].isascii()):
        return "Код рейсу має містити 2 літери та 3 цифри"

    return {
        "flight_code": code,
        "destination": destination,
        "duration": int(duration),
        "delay": int(delay),
        "passengers": int(passengers)
    }


def load_records(path):
    records = []
    errors = []

    with open(path, "r", encoding="utf-8") as file:
        for number, line in enumerate(file, 1):
            if not line.strip() or line.lstrip().startswith("#"):
                continue

            result = parse_line(line)

            if isinstance(result, dict):
                records.append(result)
            else:
                errors.append(f"Рядок {number}: {result}")

    return records, errors


def summarize(records):
    groups = {}

    for record in records:
        destination = record["destination"]
        if destination not in groups:
            groups[destination] = []

        groups[destination].append(record["delay"])

    summary = {}

    for destination, delays in groups.items():
        count = len(delays)
        total = sum(delays)

        summary[destination] = {
            "count": count,
            "total": float(total),
            "average": float(total / count),
            "max": float(max(delays)),
            "delayed_over_15_rate": sum(
                d > 15 for d in delays
            ) / count
        }

    return summary


def top_n(records, n):
    return sorted(
        records,
        key=lambda r: (-r["delay"], r["flight_code"])
    )[:n]


def unique_values(records):
    return sorted(set(r["destination"] for r in records))


def render_report(records, errors):
    summary = summarize(records)

    lines = ["--- Звіт щодо авіарейсів ---"]

    for destination in sorted(summary):
        info = summary[destination]
        lines.append(
            f"Напрямок: {destination}, "
            f"Рейсів: {info['count']}, "
            f"Середня затримка: {info['average']:.2f}"
        )

    return "\n".join(lines)


def handle_command(command, records, errors):
    if command == "1":
        return render_report(records, errors)

    elif command == "2":
        return "\n".join(unique_values(records))

    elif command == "3":
        result = top_n(records, 3)
        return "\n".join(
            f"{r['flight_code']}: {r['delay']} хв"
            for r in result
        )

    elif command == "4":
        return "\n".join(errors) if errors else "Помилок немає"

    else:
        return "Невідома команда"


def main():
    path = Path(__file__).resolve().parent.parent / "data" / "sample.txt"

    if not path.exists():
        print("Файл data/sample.txt не знайдено")
        return

    records, errors = load_records(path)

    while True:
        print("\n1. Звіт щодо авіарейсів")
        print("2. Унікальні напрямки")
        print("3. Топ-3 рейсів за затримкою")
        print("4. Помилки у файлі")
        print("0. Вихід")

        command = input("Введіть команду: ").strip()

        if command == "0":
            print("Роботу завершено")
            break

        print(handle_command(command, records, errors))


if __name__ == "__main__":
    main()
