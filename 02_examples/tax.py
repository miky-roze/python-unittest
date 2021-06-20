def calc_tax(amount, tax_rate, age):
    """Function for calculating tax"""

    # Validating types of given arguments

    if not isinstance(amount, (int, float)):
        raise TypeError(f"Amount has to be of type int or float. NOT {type(amount)}")

    if not isinstance(tax_rate, float):
        raise TypeError(f"Tax rate has to be of type float. NOT {type(tax_rate)}")

    if not isinstance(age, int):
        raise TypeError(f"Age has to be of type int. NOT {type(age)}")

    # Validating values of given arguments

    if amount < 0:
        raise ValueError(f"Amount has to be positive. Amount value: {amount}")

    if not 0 < tax_rate < 1:
        raise ValueError(f"Tax rate has to be between 0 and 1. Tax rate value: {tax_rate}")

    if age <= 0:
        raise ValueError(f"Age has to be positive. Age value: {age}")

    # Calculating tax

    if age <= 18:
        return int(min(amount * tax_rate, 5000))
    elif age <= 65:
        return amount * tax_rate
    else:
        return int(min(amount * tax_rate, 8000))
