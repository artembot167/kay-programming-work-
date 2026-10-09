def solve(income_str: str) -> str:
    income = float(income_str)

    if income < 0:
        return "Помилка: дохід не може бути від'ємним."

    if income <= 10000:
        tax = income * 0.05
    elif income <= 50000:
        tax = 10000 * 0.05 + (income - 10000) * 0.10
    else:
        tax = (10000 * 0.05 + 40000 * 0.10
               + (income - 50000) * 0.18)

    net_income = income - tax

    if income == 0:
        rate = 0
    else:
        rate = tax / income * 100

    return (f"Податок: {tax:.2f} грн\n"
            f"Чистий дохід: {net_income:.2f} грн\n"
            f"Ефективна ставка: {rate:.1f}%")


if __name__ == "__main__":
    income = input("Введіть суму доходу: ")
    print(solve(income))

    """
    Обчислює податок за прогресивною шкалою, чистий дохід та ефективну ставку.
    """
    raise NotImplementedError  # TODO: реалізуйте розв'язок за карткою


    
    
