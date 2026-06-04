# ============================================================
# BUG 1 - RUNTIME ERROR
# Type  : IndexError
# Cause : Trying to access an index that does not exist
# Fix   : Access only valid indexes (0 to 4)
# ============================================================

# BUGGY CODE:

"""
marks = []

for i in range(5):
    mark = int(input(f"Enter mark {i+1}: "))
    marks.append(mark)

# IndexError because list has only indexes 0-4
print("Sixth student's mark:", marks[5])
"""

# FIXED CODE:

marks = []

for i in range(5):
    mark = int(input(f"Enter mark {i+1}: "))
    marks.append(mark)

# Valid index
print("First student's mark:", marks[0])


# ============================================================
# BUG 2 - LOGICAL ERROR
# Type  : Logical Error
# Cause : Average calculated using wrong divisor (4 instead of 5)
# Fix   : Divide total by the actual number of students
# ============================================================

# BUGGY CODE:

"""
total = sum(marks)

# Wrong calculation
average = total / 4

print("Average Marks:", average)
"""

# FIXED CODE:

total = sum(marks)
average = total / 5

highest = max(marks)
lowest = min(marks)

print("\n------ RESULTS ------")
print("Total Marks   :", total)
print("Average Marks :", average)
print("Highest Marks :", highest)
print("Lowest Marks  :", lowest)
