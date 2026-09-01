def print_last_digit(number):
    """Print the last digit of a number"""
    number = -number if number < 0 else number
    digit = number % 10
    print(number)
    return number