def add_years_to_date(original_date, years_to_add):
    result = original_date.replace(year=original_date.year + years_to_add)
    return result

def array_sum(array):
    result = 0
    for i in array:
        result += i
    return result
