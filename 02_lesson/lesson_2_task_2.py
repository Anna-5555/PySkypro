def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


year = 2021  # Можно изменить год на любой другой
result = is_year_leap(year)


print(f"год {year}: {result}")
