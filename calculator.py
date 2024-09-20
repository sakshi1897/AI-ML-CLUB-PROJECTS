def calculate_income_tax(income):
    """
    Calculate income tax based on given income using basic progressive tax slabs.

    :param income: The total income of the individual (float or int).
    :return: Total tax amount (float).
    """

    # Define tax slabs and corresponding rates
    tax_slabs = [
        (250000, 0),  # Income up to 2,50,000 - No tax
        (500000, 0.05),  # Income between 2,50,001 to 5,00,000 - 5% tax
        (1000000, 0.2),  # Income between 5,00,001 to 10,00,000 - 20% tax
        (float('inf'), 0.3)  # Income above 10,00,000 - 30% tax
    ]

    tax = 0
    previous_limit = 0

    # Calculate tax based on slabs
    for limit, rate in tax_slabs:
        if income > limit:
            tax += (limit - previous_limit) * rate
            previous_limit = limit
        else:
            tax += (income - previous_limit) * rate
            break

    return tax


# User input
try:
    income = float(input("Enter your total income: "))
    if income < 0:
        print("Income cannot be negative.")
    else:
        tax = calculate_income_tax(income)
        print(f"The total tax on an income of {income} is: {tax:.2f}")
except ValueError:
    print("Please enter a valid number for income.")
