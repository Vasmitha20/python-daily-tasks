# Tax Calculator

def cal_tax(income):
    tax = 0
    if income <= 250000:
        tax = 0

    elif income <= 500000:
        tax = (income - 250000) * 0.05

    elif income <= 1000000:
        tax = (250000 * 0.05) + ((income - 500000) * 0.20)

    else:
        tax = (250000 * 0.05) + (500000 * 0.20) + ((income - 1000000) * 0.30)

    return tax

def tax_breakdown(income):
    taxable_income = income
    tax = cal_tax(income)

    return taxable_income, tax

income = float(input("Enter annual income: ₹"))

taxable_income, tax = tax_breakdown(income)

print("\n----- Tax Summary -----")
print(f"Taxable Income : ₹{taxable_income:.2f}")
print(f"Income Tax     : ₹{tax:.2f}")
print(f"Net Income     : ₹{(income - tax):.2f}")
