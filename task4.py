from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    result = []
    
    for user in users:
        birthday_str = user["birthday"]
        birthday = datetime.strptime(birthday_str, "%Y.%m.%d").date()
        
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_difference = (birthday_this_year - today).days
        
        if days_difference <= 7 and days_difference >= 0:
            if birthday_this_year.weekday() == 5:
                next_monday = birthday_this_year + timedelta(days=2)
                result.append({"name": user["name"], "congratulation_date": next_monday.strftime("%Y.%m.%d")})
            elif birthday_this_year.weekday() == 6:
                next_monday = birthday_this_year + timedelta(days=1)
                result.append({"name": user["name"], "congratulation_date": next_monday.strftime("%Y.%m.%d")})
            else:
                result.append({"name": user["name"], "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")})
    
    return result


users = [
    {"name": "John Doe", "birthday": "1985.09.24"},
    {"name": "John Doe", "birthday": "1985.09.26"},
    {"name": "Jane Smith", "birthday": "1990.09.28"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
