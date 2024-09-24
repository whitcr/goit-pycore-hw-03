from datetime import datetime

def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'.")

    current_date = datetime.today()

    day_difference = (given_date - current_date).days

    return day_difference

result = get_days_from_today("2021-10-09")
print(f"Кількість днів між сьогоднішньою датою та заданою: {result}")
