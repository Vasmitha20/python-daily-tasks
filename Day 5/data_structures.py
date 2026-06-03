# List
fruits = ["Apple", "Banana", "Cherry", "Orange", "Mango"]
print("1. Printing all items in List: ")
for f in fruits:
    print(f)
# Tuple
color = ("Red", "Blue", "Green")
print("\n2. Printing the first color inside Tuple: ")
print(color[0])
# Dictionary
student = {
    "Priya": 462,
    "Siri": 451,
    "Ram": 365
}
print("\n3. Displaying the student names and marks from Dictionary: ")
for key, value in student.items():
    print(f"{key}: {value}")
# Set
numbers = {24, 91, 62, 132, 91}
print("\n4. Printing all unique values in Set: ")
for i in numbers:
    print(i)
# Dictionary
stock = {
    "Laptop": 20,
    "Mobile phone": 100,
    "Headphone": 40
}
print("\n5. Displaying stock details from Dictionary: ")
for key, value in stock.items():
    print(f"{key}: {value}")
