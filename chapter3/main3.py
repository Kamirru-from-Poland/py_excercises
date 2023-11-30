import math

def count_tip(ammount, no_persons=2, percent=10):
    if ammount is None:
        raise TypeError("Missing argument: x")
    try:
        if ammount < 0:
            raise ValueError("Negative number is not allowed")
        result = ammount/(100/percent)/no_persons
        result = math.ceil(result * 100)/100
    except TypeError:
        raise TypeError("Value must be a number")
    except ValueError as ve:
        raise ValueError(ve)

    return result