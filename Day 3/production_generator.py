import random

# Input
target_units = int(input("Enter target units: "))
workers = int(input("Enter workers per shift: "))
defect_rate = float(input("Enter defect rate (%): "))

total_produced = 0
target_reached = False

# Simulate 3 shifts
for shift in range(1, 4):

    shift_produced = 0
    shift_defects = 0

    print(f"\n--- Shift {shift} ---")

    # Simulate 20 machine cycles
    for cycle in range(1, 21):

        # Check if target already reached
        if total_produced >= target_units:
            target_reached = True
            break

        # Randomly determine if item is defective
        if random.randint(1, 100) <= defect_rate:
            shift_defects += 1
            continue

        # Good item produced
        shift_produced += 1
        total_produced += 1

    # Worker productivity
    productivity = shift_produced / workers

    print("Items Produced:", shift_produced)
    print("Defective Items:", shift_defects)
    print("Worker Productivity:", round(productivity, 2), "units/worker")

    # Stop all production
    if target_reached:
        print("\nProduction target reached. Stopping all shifts.")
        break

# Final report
print("\n===== Production Summary =====")
print("Target Units:", target_units)
print("Total Good Units Produced:", total_produced)
print("Production Completed:", total_produced >= target_units)
