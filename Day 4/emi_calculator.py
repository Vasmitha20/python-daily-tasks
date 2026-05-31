# EMI Calculator

def cal_emi(principal, rate, tenure):
    monthly_rate = rate / (12 * 100)
    months = tenure * 12

    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / \
          ((1 + monthly_rate) ** months - 1)

    return emi

principal = float(input("Enter loan amount: "))
rate = float(input("Enter annual interest rate (%): "))
tenure = float(input("Enter loan tenure (in years): "))

emi = cal_emi(principal, rate, tenure)

print(f"\nMonthly EMI: ₹{emi:.2f}")

