# Enhanced Loan Eligibility System

age = int(input("Enter your age: "))
salary = int(input("Enter your salary: "))
emp = int(input("Enter 1 for Salaried, 2 for Self-Employed and 3 for other: "))

if (age < 21 or age > 60):
    print("Rejected: Age criteria not met.")
elif salary < 25000:
    print("Rejected: Salary criteria not met.")
elif (emp not in [1, 2] or emp == 3):
    print("Rejected: Employment type must be either salaried or self-employed.")
else:
    if (21 <= age <= 30 and salary < 30000):
        print("Needs guarantor.")
    elif (age > 55 and emp == 2):
        print("High risk, senior review needed.")
    else:
        print("Approved!")
