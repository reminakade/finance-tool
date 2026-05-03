def currency_convert(amount, rate):
    """Converts amount using exchange rate."""
    return amount * rate

def simple_interest(principal, rate, years):
    """Calculates simple interest."""
    return principal * rate * years / 100

if __name__ == "__main__":
    print(currency_convert(100, 4.2))
    print(simple_interest(1000, 5, 3))