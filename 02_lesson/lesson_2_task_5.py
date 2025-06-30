def month_to_season(m):
    if 3 <= m <= 5:
        return "весна"
    elif 6 <= m <= 8:
        return "лето"
    elif 9 <= m <= 11:
        return "осень"
    elif 1 <= m <= 2:
        return "зима"
    elif m <= 12:
        return "зима"
    else:
        return " Неверный номер месяца"


try:
    m = int(input("Введите номер месяца (1-12):  "))
    print(month_to_season(m))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")
