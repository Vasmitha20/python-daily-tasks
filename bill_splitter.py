# Bill-Splitting Calculator

# Input from user
tot_bill = float(input("Enter total bill amount: "))
people = int(input("Enter the number of people: "))
tip_percentage = float(input("Enter the tip percentage: "))

# Calculating tip amount, total amount with tip and amount per person
tip_amt = (tot_bill * tip_percentage) / 100
tot_with_tip = tot_bill + tip_amt
amt_per_person = tot_with_tip / people

# Using remaining arithmetic operators (-, %)
difference = tot_with_tip - tot_bill
remainder = tot_with_tip % people

# Rounding the result to 2 decimal places using round()
tip_amt = round(tip_amt, 2)
tot_with_tip = round(tot_with_tip, 2)
amt_per_person = round(amt_per_person, 2)

# Printing summary
print("\n============ BILL SUMMARY ============")
print(f"Original Bill Amount   : ₹{tot_bill}")
print(f"Tip Percentage         : {tip_percentage}%")
print(f"Tip Amount             : ₹{tip_amt}")
print(f"Total with Tip         : ₹{tot_with_tip}")
print(f"Number of People       : {people}")
print(f"Amount per Person      : ₹{amt_per_person}")
print(f"Added Tip              : ₹{difference}")
print(f"Remainder              : ₹{remainder}")
print("========================================")