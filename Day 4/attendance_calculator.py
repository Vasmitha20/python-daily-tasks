# Attendance Calculator

def cal_attendance(attended, total):
    percentage = (attended / total) * 100
    return percentage

def classes_needed(attended, total, target):
    future_classes = 0

    while ((attended + future_classes) / (total + future_classes)) * 100 < target:
        future_classes += 1

    return future_classes

attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes conducted: "))
target = float(input("Enter required attendance percentage: "))

attendance = cal_attendance(attended, total)

print("\n----- Attendance Report -----")
print(f"Attendance Percentage: {attendance:.2f}%")

if attendance >= target:
    print("Requirement Status: Met")
else:
    print("Requirement Status: Not Met")

    needed = classes_needed(attended, total, target)
    print(f"Classes to Attend for {target:.0f}% Attendance: {needed}")

    
