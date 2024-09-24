import random

def get_numbers_ticket(min, max, quantity):

    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
    
    unique_numbers = set()
    
    while len(unique_numbers) < quantity:
        number = random.randint(min, max)
        unique_numbers.add(number)

    return sorted(unique_numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
