def count_all(hours, rate):

    income = hours * rate
    tax = income * 0.2
    superd = income * 0.1
    return income, tax, superd

def convert_to_num(num):
    try:
        return int(num)
    except ValueError:
        try:
            return float(num)
        except ValueError:
            return 0
